from rest_framework import permissions
from tournoi.models import Tournament

class IsAdminTournament(permissions.BasePermission):
    def has_permission(self, request, view):
        tournoi = Tournament.objects.get(id = request.ID)
        admins = tournoi.admin.all()
        if request.user.is_authenticated and (request.user in admins or request.user.is_admin):
            return True
        else:
            return False