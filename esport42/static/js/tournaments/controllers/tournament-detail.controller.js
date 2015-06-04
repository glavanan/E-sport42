/**
 * Created by cwagner on 16/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.tournaments.controllers')
        .controller('TournamentDetailController', TournamentDetailController);
        //.controller('TournamentDetailController', function (Tournaments, tournament, $stateParams) {
        //    console.log(tournament);
        //    //console.log($stateParams);
        //});

    TournamentDetailController.$inject = ['tournament', 'Authentication', '$state'];

    function TournamentDetailController(tournament, Authentication, $state) {
        var vm = this;
        vm.me = null;
        vm.register = register;

        activate();

        function activate() {
            vm.tournament = tournament;
            vm.me = Authentication.getAuthenticatedAccount();
        }

        function register () {
            if (vm.me)
                $state.go('tournament-detail.register');
            else
                console.log('go fuck yourself');
        }

    }
})();