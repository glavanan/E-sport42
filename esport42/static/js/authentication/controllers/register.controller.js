/**
 * Created by cwagner on 25/02/2015.
 */

(function () {
    angular
        .module('esport42.authentication.controllers')
        .controller('RegisterController', RegisterController);

    RegisterController.$inject = ['$location', '$scope', 'Authentication'];

    function RegisterController($location, $scope, Authentication) {
        var vm = this;

        vm.form = {
            email : null,
            password : null,
            username: null,
            firstName: null,
            lastName: null,
            address : null,
            birthDate: null,
            nationality: null,
            phone: null
        }
        vm.register = register;

        function register() {
            if (vm.form.password == vm.password2) {
                console.log('In register function bitch');
                Authentication.register(vm.email, vm.password, vm.username)
                    .success(function (data, status, headers, config) {
                        alert('You have been registered');
                        // this callback will be called asynchronously
                        // when the response is available
                    })
                    .error(function (data, status, headers, config) {
                        alert('Something was wrong. Maybe it\'s your username');
                        console.log('KAKA');
                        // called asynchronously if an error occurs
                        // or server returns response with an error status.
                    });
            }
            else
                alert("Both passwords are different");
        }
    }
})();
