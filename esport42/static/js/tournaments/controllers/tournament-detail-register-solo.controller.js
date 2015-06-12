/**
 * Created by cwagner on 16/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.tournaments.controllers')
        .controller('TournamentDetailRegisterSoloController', TournamentDetailRegisterSoloController);

    TournamentDetailRegisterSoloController.$inject = ['tournament', 'Authentication'];

    function TournamentDetailRegisterSoloController(tournament, Authentication) {
        var vm = this;
        vm.register = register;
        vm.me = null;

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
            Tournaments.submitTeam(vm.tournament.id, vm.form)
                .then(function (data, status, headers, config) {
                    vm.submitionOk = true;
                    vm.teamId = data['id'];
                }, function (data, status, headers, config) {

                });
        }
    }
})();