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

        function logout() {
            if (Authentication.isAuthenticated())
                Authentication.logout();
            return false;
        }
    }
})();