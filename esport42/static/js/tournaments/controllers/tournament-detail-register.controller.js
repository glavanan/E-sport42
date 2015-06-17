/**
 * Created by cwagner on 16/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.tournaments.controllers')
        .controller('TournamentDetailRegisterController', TournamentDetailRegisterController);

    TournamentDetailRegisterController.$inject = ['tournament', 'Users', 'Tournaments', 'Authentication', '_', '$sce'];

    function TournamentDetailRegisterController(tournament, Users, Tournaments, Authentication, _, $sce) {
        var vm = this;

        vm.register = register;
        vm.submtionOk = false;
        vm.users = [];
        vm.tournament = null;
        vm.me = null;
        vm.form = {};
        vm.form.members = [];
        vm.paypalReturnUrl = $sce.trustAsResourceUrl("http://esport.42.fr");
        vm.paypalUrl = $sce.trustAsResourceUrl("https://www.paypal.com/cgi-bin/webscr");
        vm.addNewUser = addNewUser;
        vm.EMAIL_REGEXP = /^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/i;

        activate();

        function activate() {
            vm.tournament = tournament;
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
            if (vm.readRules !== true) {vm.readRules = false;
                return;
            }
            vm.toSend = angular.copy(vm.form);
            vm.form.members = _.pluck(vm.form.members, 'id');
            vm.form.admin = vm.me.id;
            Tournaments.submitTeam(vm.tournament.id, vm.form)
                .then(function (data, status, headers, config) {
                    vm.submitionOk = true;
                    vm.teamId = data['id'];
                }, function (data, status, headers, config) {

                });
        }

        function addNewUser() {
            function randomPassword(length) {
                var chars = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()-+<>ABCDEFGHIJKLMNOP1234567890";
                var pass = "";
                for (var x = 0; x < length; x++) {
                    var i = Math.floor(Math.random() * chars.length);
                    pass += chars.charAt(i);
                }
                return pass;
            }

            var user = vm.newUser;
            user.password = randomPassword(5);
            user.password_confirm = user.password;
            Authentication.register(user)
                .then(function (data, status, headers, config) {
                    vm.form.members.push(data);
                    vm.newUser = {};
                    vm.addNewPlayer = false;
                }, function (data, status, headers, config) {
                    console.log(data);
                });
        }
    }
})();
