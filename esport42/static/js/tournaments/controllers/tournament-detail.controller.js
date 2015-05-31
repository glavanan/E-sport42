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

    TournamentDetailController.$inject = ['Tournaments', 'tournament', '$sce'];

    function TournamentDetailController(Tournaments, tournament, $sce) {
        var vm = this;

        vm.tournaments = [];

        activate();

        function activate() {
            vm.tournament = tournament;
            //console.log(vm.tournament);
            //console.log(vm.test);
            //vm.test = $sce.trustAsHtml(vm.test);
            //console.log(vm.test);
        }

    }
})();