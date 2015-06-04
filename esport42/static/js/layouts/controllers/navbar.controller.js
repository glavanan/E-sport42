/**
 * Created by oddnaughty on 3/14/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.layouts.controllers')
        .controller('NavbarController', NavbarController);

    NavbarController.$inject = ['$scope', 'Authentication', 'Tournaments'];

    function NavbarController($scope, Authentication, Tournaments) {
        var vm = this;

        vm.logout = logout;
        vm.goHomeYoureDrunk = home;

        activate();

        function activate() {
            $scope.$watch(function (scope) {return scope.userIsAuthenticated}, onUserChange);
            Tournaments.all()
                .then(function (data, status) {
                    vm.tournaments = data;
                    var test = window.encodeURIComponent(data[0].name);
                }, function (data, status) {
                    console.log("Get tournaments failed in NavBarController: ", data);
                })
        }

        function logout() {
            if (Authentication.isAuthenticated())
                Authentication.logout();
            return false;
        }

        function onUserChange(newValue) {
            if (newValue === false)
                Authentication.unauthenticate();
        }

        function home() {
                                window.location = '/home';

        }
    }
})();