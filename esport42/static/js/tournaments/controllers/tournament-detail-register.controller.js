/**
 * Created by cwagner on 16/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.tournaments.controllers')
        .controller('TournamentDetailRegisterController', TournamentDetailRegisterController);

    TournamentDetailRegisterController.$inject = ['tournament', 'Users', 'Tournaments'];

    function TournamentDetailRegisterController(tournament, Users, Tournaments) {
        var vm = this;

        vm.register = register;
        vm.submtionOk = false;

        activate();

        function activate() {
            vm.tournament = tournament[0];
            vm.users = [];
            Users.all()
                .then(function (data, status) {
                    vm.users = data;
                }, function (data, status) {
                    console.log("I failed to getting all users in the controller :(", data);
                });
            console.log(vm.users);

        }

        function register() {
            console.log("U did register biatch !", vm.form.members);
            Tournaments.submitTeam(vm.tournament.id, vm.form)
                .then(function (data, status, headers, config) {
                    console.log("Team submitted, easy as shit !", data);
                    vm.submitionOk = true;
                }, function (data, status, headers, config) {

                });
        }
    }
})();


//{ Name, Tag, Members }