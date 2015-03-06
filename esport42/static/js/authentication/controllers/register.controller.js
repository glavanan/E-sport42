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

        vm.register = register;

        function register() {
            if (vm.password == vm.password2) {
                console.log('In register function bitch');
                Authentication.register(vm.email, vm.password, vm.username)
                    .success(function (data, status, headers, config) {
                        console.log(data, status, headers, config);
                        // this callback will be called asynchronously
                        // when the response is available
                    })
                    .error(function (data, status, headers, config) {
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
