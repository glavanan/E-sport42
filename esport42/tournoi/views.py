from django.shortcuts import render
from base.models import Payments, MyUser
from rest_framework.response import Response
from tournoi.models import Tournament, Teams, Phase, TPost, APost
from match.models import Match
from tournoi.serializers import TournamentSerializer, PhaseSerializer, TeamSerializer, TPostSerializer, APostSerializer
from post.permissions import IsAdminOfSite, IsTornamentOrAdmin
from match.permissions import IsAdminTournament
from rest_framework import permissions, viewsets, status, views, permissions
import urllib
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import View
from rest_framework.decorators import detail_route
from django.core import serializers
from rest_framework.renderers import JSONRenderer
import logging
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from rest_framework_extensions.decorators import action
from rest_framework import viewsets
from rest_framework import status
from esport42.settings import ADMINS
import math
import random

logger = logging.getLogger(__name__)


class APostViewSet(viewsets.ModelViewSet):
    queryset = APost.objects.all()
    serializer_class = APostSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return APost.objects.filter(tournament=self.kwargs['parent_lookup_tournoi'])

    def get_permissions(self):
        self.request.ID = self.kwargs['parent_lookup_tournoi']
        if self.request.method == 'GET':
            return [permissions.AllowAny(), ]
        else:
            return [IsTornamentOrAdmin(), ]

    def perform_create(self, serializer):
        instance = serializer.save(author=self.request.user,
                                   tournament=Tournament.objects.get(id=self.kwargs['parent_lookup_tournoi']))
        return super(APostViewSet, self).perform_create(serializer)


class TPostViewSet(viewsets.ModelViewSet):
    queryset = TPost.objects.all()
    serializer_class = TPostSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return TPost.objects.filter(tournament=self.kwargs['parent_lookup_tournoi'])

    def get_permissions(self):
        self.request.ID = self.kwargs['parent_lookup_tournoi']
        if self.request.method == 'GET':
            return [permissions.AllowAny(), ]
        else:
            return [IsTornamentOrAdmin(), ]

    def perform_create(self, serializer):
        instance = serializer.save(author=self.request.user,
                                   tournament=Tournament.objects.get(id=self.kwargs['parent_lookup_tournoi']))
        return super(TPostViewSet, self).perform_create(serializer)

class PhaseViewSet(viewsets.ModelViewSet):
    serializer_class = PhaseSerializer
    queryset = Phase.objects.all()

    def get_queryset(self):
        return Phase.objects.filter(tournament=self.kwargs['parent_lookup_tournoi'])

    def get_permissions(self):
        self.request.ID = self.kwargs['parent_lookup_tournoi']
        if self.request.method == 'GET':
            return [permissions.AllowAny(),]
        if self.request.method == 'POST':
            return [IsAdminTournament(), ]
        return [permissions.IsAdminUser(), ]

    @detail_route(methods=['post'])
    def fill_phase(self, request, pk=None, parent_lookup_tournoi=None):
        phase = Phase.objects.get(id=pk)
        tournoi = Tournament.objects.get(id=parent_lookup_tournoi)
        print pk
        print parent_lookup_tournoi
        print phase.order
        teams = list(Teams.objects.filter(verified=True, tournament=parent_lookup_tournoi).order_by("score"))
        matchs = list(Match.objects.filter(phase=pk).order_by("level", "match_number"))
        if phase.name == "Pool":
            matchs = list(Match.objects.filter(phase=pk).order_by("level", "match_number"))

            number = 0
            turn = 0
            for team in teams:
                if number == 0:
                    matchs[0 + (turn * 4)](team1=team)
                    matchs[2 + (turn * 4)](team1=team)
                    matchs[4 + (turn * 4)](team1=team)
                if number == 1:
                    matchs[0 + (turn * 4)](team2=team)
                    matchs[3 + (turn * 4)](team1=team)
                    matchs[5 + (turn * 4)](team1=team)
                if number == 2:
                    matchs[1 + (turn * 4)](team1=team)
                    matchs[2 + (turn * 4)](team2=team)
                    matchs[5 + (turn * 4)](team2=team)
                if number == 3:
                    matchs[1 + (turn * 4)](team2=team)
                    matchs[3 + (turn * 4)](team2=team)
                    matchs[4 + (turn * 4)](team2=team)
                if number < 3:
                    number += 1
                else:
                    number = 0
                    turn += 1
        elif phase.name == "DTree":
            matchs = list(Match.objects.filter(phase=pk, level=0.0, looser_braket=False).order_by("level", "match_number"))
            print "tree"
            nb_matchs = tournoi.nbteams / 2
            match_per_pool = nb_matchs / 4
            number_match = 0
            i = 0
            for item in matchs:
                print item.id
            print matchs[0].id
            for team in teams:
                if i % 4 == 0 or i % 4 == 3:
                    number_match = (i * match_per_pool)
                elif i % 4 == 1:
                    number_match = ((i + 1) * match_per_pool)
                else:
                    number_match = ((i - 1) * match_per_pool)
                print number_match
                if (i / 4) % 2 == 0:
                    while matchs[number_match].team1:
                        number_match += 1
                    matchs[number_match].team1 = team
                    matchs[number_match].team2 = teams[-i - 1]
                    matchs[number_match].save()
                else:
                    number_match += match_per_pool - 1
                    while matchs[number_match].team1:
                        number_match -= 1
                    matchs[number_match].team1 = team
                    matchs[number_match].team2 = teams[-i - 1]
                    matchs[number_match].save()
                i += 1



def create_match(phase, tournoi):
    print "create match"
    if phase.name == 'DTree':
        print "entrance"
        i = 0;
        nb_match = tournoi.nbteams / 2
        round = int(math.ceil(math.log(tournoi.nbteams, 2)))
        print "round ="
        print round
        while i <= round:
            print "i = "
            print i
            n = 0
            while n < (nb_match * 2) / (2**(i + 1)):
                m1 = Match(level=i, match_number=n, phase=phase, looser_braket=False)
                m1.save()
                if i != 0:
                    m2 = Match(level=i, match_number=n, phase=phase, looser_braket=True)
                    m2.save()
                    if n < nb_match / (2**(i + 1)) or i == round - 1:
                        m2 = Match(level=i + 0.5, match_number=n, phase=phase, looser_braket=True)
                        m2.save()
                elif n < nb_match / (2**(i + 1)):
                    m2 = Match(level=i, match_number=n, phase=phase, looser_braket=True)
                    m2.save()
                n = n + 1
            i = i + 1
            m2 = Match(level=round, match_number=0, phase=phase, looser_braket=True)
            m2.save()
    elif phase.name == 'Pool':
        nb_participant = 4
        nb_poule = tournoi.nbteams / nb_participant
        nb_match = nb_participant * (nb_participant + 1) / 2 - nb_participant
        round = 0
        while round < nb_poule:
            match = 0
            while match < nb_match:
                m1 = Match(level=round, match_number=match, phase=phase)
                m1.save()
                match += 1
            round += 1
                






class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    lookup_field = 'id'

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny(), ]
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated(), ]
        return [permissions.IsAdminUser(), ]


    def create(self, request, **kwargs):
        type = request.data['type']
        serializer = self.serializer_class(data=request.data)
        print type
        if serializer.is_valid():
            serializer.validated_data.pop('type')
            tournoi = serializer.save()
            print type
            number = 0
            tmp = Phase(name=type, tournament=tournoi, order=number)
            tmp.save()
            create_match(tmp, tournoi)
            serializer.validated_data.pop('admin')
            serializer.validated_data.pop('rules')
            # Je doit retourenr le validated data - User !!!
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamsViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects.all()

    serializer_class = TeamSerializer

    def get_queryset(self):
        return Teams.objects.filter(tournament=self.kwargs['parent_lookup_tournoi'])

    def get_permissions(self):
        self.request.ID = self.kwargs['parent_lookup_tournoi']
        if self.request.method == 'GET':
            return [permissions.AllowAny(), ]
        elif self.request.method == 'POST':
            return [permissions.IsAuthenticated(), ]
        else:
            return [IsAdminOfSite(), ]

    def perform_create(self, serializer):
        serializer.save(tournament=Tournament.objects.get(id=self.kwargs['parent_lookup_tournoi']))
        return super(TeamsViewSet, self).perform_create(serializer)

    def create(self, request, **kwargs):
        serial = self.serializer_class(data=request.data)
        tournoi = Tournament.objects.get(id=self.kwargs['parent_lookup_tournoi'])
        if serial.is_valid():
            if len(serial.validated_data['members']) >= tournoi.player_per_team and len(
                    serial.validated_data['members']) <= tournoi.max_player:
                serial.save(tournament=tournoi)
                serial.validated_data['members'] = [user.id for user in serial.validated_data['members']]
                serial.validated_data['admin'] = serial.validated_data['admin'].id
                serial.validated_data['tournament'] = tournoi.id
                serial.validated_data['id'] = serial.data['id']
                return Response(serial.validated_data, status=status.HTTP_201_CREATED)
            return Response({"error": "Not enough member"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def ipn(request):
    admins_mails = [admin[1] for admin in ADMINS]

    if request.method == 'POST':
        data = dict(request.POST)
        for k in data:
            data[k] = data[k][0].encode('utf-8')
        tmp = urllib.urlopen("https://www.paypal.com/cgi_bin/websrc",
                             'cmd=_notify-validate&' + urllib.urlencode(data)).read()
        if tmp == 'VERIFIED':
            if data['payment_status'] == 'Completed' and 'custom' in data.keys() and data['custom']:
                team = Teams.objects.get(id=int(data['custom']))
                if not Teams.objects.filter(txn_id=data['txn_id']) and data[
                    'receiver_email'] == team.tournament.receiver_email and float(data['mc_gross']) == float(
                        team.tournament.price) and data['payment_status'] == 'Completed' and data[
                    'mc_currency'] == 'EUR':
                    team.verified = True
                    team.txn_id = data['txn_id']
                    team.save()
                    msg = EmailMessage(subject="Inscription valide", from_email="noreply@esport.42.fr", to=[team.admin.email], bcc=admins_mails)
                    msg.global_merge_vars={'NAME1' : team.admin.username, 'NAMETOURNOI' : team.tournament.name}
                    msg.template_name="base"

                    msg.send()
                    return HttpResponse("team verified")
                logger.debug("almost")
                return HttpResponse("team not valid")
        else:
            logger.debug("ret")
        return HttpResponse("OK")
    else:
        logger.debug("get")
        return HttpResponse(
            '<form method="post" action="https://www.sandbox.paypal.com/cgi-bin/webscr" class="paypal-button" target="_top" style="opacity: 1;"><div class="hide" id="errorBox"></div><input type="hidden" name="button" value="buynow"><input type="hidden" name="business" value="42.esport1@gmail.com"><input type="hidden" name="item_name" value="tournoi"><input type="hidden" name="quantity" value="1"><input type="hidden" name="amount" value="50"><input type="hidden" name="currency_code" value="EUR"><input type="hidden" name="shipping" value="0"><input type="hidden" name="tax" value="0"><input type="hidden" name="notify_url" value="http://danstonpi.eu/api/ret/ipn"><input type="hidden" name="cancel_url" value="http://danstonpi.eu/cancel"><input type="hidden" name="return_url" value="http://danstonpi.eu/done"><input type="hidden" name="cmd" value="_xclick"><input type="hidden" name="bn" value="JavaScriptButton_buynow"><input type="hidden" name="custom" value="26"/><button type="submit" class="paypal-button large">Buy Now</button></form>')


@csrf_exempt
def ipn_test(request):
    admins_mails = [admin[1] for admin in ADMINS]

    def tournaments_pay_user(pp_obj, data_post):
        tournament = Tournament.objects.get(id=pp_obj.id_event)
        user = MyUser.objects.get(id=pp_obj.id_payer)
        if tournament and user:
            if float(data_post['mc_gross']) == float(tournament.price) and data_post['mc_currency'] == "EUR":
                pp_obj.txn_id = data_post['txn_id']
                pp_obj.verified = True
                pp_obj.save()
                tournament.pool.add(user)
                tournament.save()
                msg = EmailMessage(subject="Inscription valide", from_email="noreply@esport.42.fr", to=[user.email], bcc=admins_mails)
                msg.global_merge_vars={'NAME1' : user.username, 'NAMETOURNOI' : tournament.name}
                msg.template_name="base"
                ret = msg.send()
                if ret != 1:
                    logger.debug("Message non envoye a: {} pour le tournoi: {}".format(user.email, tournament.name))
                return HttpResponse("Payment accepted")
        else:
            logger.debug("No tournament ({}) or user({})".format(tournament, user))
        return HttpResponse("There was shit in da payment")

    def tournaments_pay_team(pp_obj, data_post):
        tournament = Tournament.objects.get(id=pp_obj.id_event)
        team = Teams.objects.get(id=pp_obj.id_payer)
        if tournament and team:
            if float(data_post['mc_gross']) == float(tournament.price) and data_post['mc_currency'] == "EUR":
                pp_obj.txn_id = data_post['txn_id']
                team.txn_id = data_post['txn_id']
                pp_obj.verified = True
                pp_obj.save()
                team.save()
                msg = EmailMessage(subject="Inscription valide", from_email="noreply@esport.42.fr", to=[team.admin.email], bcc=admins_mails)
                msg.global_merge_vars= {'NAME1': team.admin.username, 'NAMETOURNOI': tournament.name}
                msg.template_name= "base"
                ret = msg.send()
                if ret != 1:
                    logger.debug("Message non envoye a: {} pour le tournoi: {}".format(team.admin.email, tournament.name))
                return HttpResponse("Payment accepted")
        else:
            logger.debug("No tournament ({}) or team.admin ({})".format(tournament, team.admin))
        return HttpResponse("There was shit in da payment")

    methods_funcs = {
        "Tournament": {
            "Teams": tournaments_pay_team,
            "MyUser": tournaments_pay_user
        }
    }

    if request.method == "POST":
        data = dict(request.POST)
        for k in data:
            data[k] = data[k][0].encode('utf-8')
        tmp = urllib.urlopen("https://www.paypal.com/fr/cgi-bin/webscr",
                             'cmd=_notify-validate&' + urllib.urlencode(data)).read()
        if tmp == "VERIFIED":
            if data['payment_status'] == 'Completed' and 'custom' in data.keys() and data['custom']:
                paypal_object = Payments.objects.get(id=int(data['custom']))
                if not paypal_object:
                    logger.debug("No paypal object for this request. Request data: {}".format(data))
                    return HttpResponse("No payment in our database")
                if paypal_object.txn_id:
                    logger.debug("Payment already done for this request. Request data: {}".format(data))
                    return HttpResponse("The payment is already done")
                if paypal_object.payment_to != data['receiver_email']:
                    logger.debug("Receiver email is different for this request. Request data: {}".format(data))
                    return HttpResponse("Receiver_email is wrong")
                return methods_funcs[paypal_object.type_event][paypal_object.type_payer](paypal_object, data)
            else:
                logger.debug("Payment was not completed. Request data: {}".format(data))
                return HttpResponse("Payment was not completed")
        else:
            logger.debug("Payment was not Paypal verified. tmp: {}, data: {}".format(tmp, data))
            return HttpResponse("Paypal said no.")
    else:
        return HttpResponse("""<form action="https://www.sandbox.paypal.com/cgi-bin/webscr" method="post" target="_top">
<input type="hidden" name="cmd" value="_xclick">
<input type="hidden" name="business" value="42.esport1@gmail.com">
<input type="hidden" name="lc" value="FR">
<input type="hidden" name="item_name" value="test_solo_tournament_payment2">
<input type="hidden" name="amount" value="10.00">
<input type="hidden" name="currency_code" value="EUR">
<input type="hidden" name="button_subtype" value="services">
<input type="hidden" name="no_note" value="1">
<input type="hidden" name="no_shipping" value="1">
<input type="hidden" name="rm" value="1">
<input type="hidden" name="return" value="http://danstonpi.eu/done">
<input type="hidden" name="cancel_return" value="http://danstonpi.eu/cancel">
<input type="hidden" name="bn" value="PP-BuyNowBF:btn_buynowCC_LG.gif:NonHosted">
<input type="hidden" name="notify_url" value="http://danstonpi.eu/api/ret/ipn">
<input type="image" src="https://www.sandbox.paypal.com/fr_FR/FR/i/btn/btn_buynowCC_LG.gif" border="0" name="submit" alt="PayPal - la solution de paiement en ligne la plus simple et la plus securisee">
<img alt="" border="0" src="https://www.sandbox.paypal.com/fr_FR/i/scr/pixel.gif" width="1" height="1">
</form>""")


@csrf_exempt
def ipn_return(request):
    def tournament_return_team(paypal_object, team=None):
        if not team:
            team = Teams.objects.get(id=paypal_object.id_payer)
        return redirect("http://" + request.META['HTTP_HOST'] + "/tournaments/" + team.tournament.tag + "/register-success?teamName=" + team.name)

    def tournament_return_solo(paypal_object):
        tournament = Tournament.objects.get(id=paypal_object.id_event)
        user = MyUser.objects.get(id=paypal_object.id_payer)
        return redirect("http://" + request.META['HTTP_HOST'] + "/tournaments/" + tournament.tag + "/register-success?teamName=" + user.username)

    methods_funcs = {
        "Tournament": {
            "Teams": tournament_return_team,
            "MyUser": tournament_return_solo
        }
    }
    if request.method == "POST":
        payment_id = request.POST['custom']
        if payment_id:
            try:
                payment = Payments.objects.get(id=int(payment_id))
                if not payment.verified:
                    team = Teams.objects.filter(id=int(payment_id))
                    if not team:
                        return tournament_return_solo(payment)
                    return tournament_return_team(None, team[0])
            except Payments.DoesNotExist as e:
                logger.debug("{}\nId received: {}\nPOST data: {}".format(e, payment_id, request.POST))
                team = Teams.objects.get(id=int(payment_id))
                return tournament_return_team(None, team)
        else:
            return redirect(request.get_host())
        return methods_funcs[payment.type_event][payment.type_payer](payment)
    elif request.method == "GET":
        return HttpResponse(request.get_host())
    else:
        return redirect(request.get_host())


class TeamExists(views.APIView):
    def get(self, request):
        teamname = request.GET.get('name', None)
        tournament = request.GET.get('tournament', None)
        print tournament
        if teamname and tournament and not Teams.objects.filter(name=teamname, tournament=tournament):
            return Response({}, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class TagExists(views.APIView):
    def get(self, request):
        teamname = request.GET.get('name', None)
        tournament = request.GET.get('tournament', None)
        print tournament
        if teamname and tournament and not Teams.objects.filter(tag=teamname, tournament=tournament):
            return Response({}, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

# Create your views here.
