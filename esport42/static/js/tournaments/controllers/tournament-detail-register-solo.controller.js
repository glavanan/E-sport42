/**
 * Created by cwagner on 16/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.tournaments.controllers')
        .controller('TournamentDetailRegisterSoloController', TournamentDetailRegisterSoloController);

    TournamentDetailRegisterSoloController.$inject = ['tournament', 'Authentication', 'Tournaments', '$sce'];

    function TournamentDetailRegisterSoloController(tournament, Authentication, Tournaments, $sce) {
        var vm = this;
        vm.register = register;
        vm.me = null;
        vm.paymentTo = "42.esport@gmail.com";
        vm.paypalUrl = $sce.trustAsResourceUrl("https://www.paypal.com/cgi-bin/webscr");
        vm.paypalReturnUrl = $sce.trustAsResourceUrl("http://esport.42.fr");

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