/**
 * Created by cwagner on 16/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.tournaments.controllers')
        .controller('TournamentDetailRegisterController', TournamentDetailRegisterController);

    TournamentDetailRegisterController.$inject = ['tournament', 'Users', 'Tournaments', 'Authentication', '_'];

    function TournamentDetailRegisterController(tournament, Users, Tournaments, Authentication, _) {
        var vm = this;

        vm.register = register;
        vm.submtionOk = false;
        vm.users = [];
        vm.tournament = null;
        vm.me = null;
        vm.form = {};
        vm.form.members = [];

        activate();

        function activate() {
            vm.tournament = tournament;
            console.log("Tournament:", tournament);
            Users.all()
                .then(function (data, status) {
                    vm.users = data;
                }, function (data, status) {
                    console.log("I failed to getting all users in the controller :(", data);
                });
            vm.me = Authentication.getAuthenticatedAccount();
            vm.form.members.push(vm.me);
        }

        function register() {
            vm.form.members = _.pluck(vm.form.members, 'id');
            vm.form.admin = vm.me.id;
            Tournaments.submitTeam(vm.tournament.id, vm.form)
                .then(function (data, status, headers, config) {
                    vm.submitionOk = true;
                }, function (data, status, headers, config) {

                });
        }
    }
})();


//{ Name, Tag, Members }