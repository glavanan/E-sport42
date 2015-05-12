/**
 * Created by oddnaughty on 3/14/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.layouts.controllers')
        .controller('NavbarController', NavbarController);

    NavbarController.$inject = ['$scope', 'Authentication'];

    function NavbarController($scope, Authentication) {
        var vm = this;

        vm.logout = logout;

        activate();

        function activate() {
            $scope.$watch(function (scope) {return scope.userIsAuthenticated}, onUserChange);
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
    }
})();