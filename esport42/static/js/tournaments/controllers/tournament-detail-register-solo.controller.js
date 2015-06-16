/**
 * Created by cwagner on 16/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.tournaments.controllers')
        .controller('TournamentDetailRegisterSoloController', TournamentDetailRegisterSoloController);

    TournamentDetailRegisterSoloController.$inject = ['tournament', 'Authentication', 'Tournaments'];

    function TournamentDetailRegisterSoloController(tournament, Authentication, Tournaments) {
        var vm = this;
        vm.register = register;
        vm.me = null;
        vm.paymentTo = "42.esport1@gmail.com";
        vm.paypalUrl = "https://www.sandbox.paypal.com/cgi-bin/webscr";
        vm.paypalReturnUrl = "http://danstonpi.eu";

        activate();

        function activate() {
            vm.tournament = tournament;
            vm.me = Authentication.getAuthenticatedAccount();
        }

        function register() {
            if (vm.readRules !== true) {
                vm.readRules = false;
                return;
            }
            var user = vm.me.id;
            Tournaments.submitSolo(vm.tournament.id, user, vm.paymentTo)
                .then(function (data, status, headers, config) {
                    vm.customValue = data.id;
                    vm.submitionOk = true;
                }, function (data, status, headers, config) {

                });
        }
    }
})();