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
        vm.me = null;

        activate();

        function activate() {
            vm.tournament = tournament;
            vm.me = Authentication.getAuthenticatedAccount();
        }

    }
})();