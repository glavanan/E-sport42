/**
 * Created by cwagner on 25/02/2015.
 */

(function () {
    console.log("wiwiwiw");
    angular
        .module('esport42.site.controllers')
        .controller('RegisterController', RegisterController);

    RegisterController.$inject = ['$location', '$scope'];

    function RegisterController($location, $scope) {
        var vm = this;

        vm.register = register;

        function register() {
            console.log('In register function bitch');
        }
    }
})