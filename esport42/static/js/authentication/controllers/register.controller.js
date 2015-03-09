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
        };
        vm.registerMandatory = registerMandatory;
        vm.registerOptional = registerOptional;
        vm.next = false;
        vm.EMAIL_REGEXP = /^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/i;

        function registerMandatory(isValid) {
            if (!isValid)
                return ;
            else if (vm.form.password && vm.form.password == vm.passwordConfirm) {
                vm.next = true;
                //Authentication.register(vm.form.email, vm.form.password, vm.form.username)
                //    .success(function (data, status, headers, config) {
                //        alert('You have been registered');
                //        vm.next = true;
                //    })
                //    .error(function (data, status, headers, config) {
                //        alert('Something was wrong. Maybe it\'s your username');
                //        console.log('KAKA');
                //    });
            }
            else
                alert("Both passwords are different");
        }

        function registerOptional(isValid) {
            console.log("je passe dedans: ", isValid);
            if (!isValid)
                return ;
            console.log('Registering Optional fields');
        }
    }
})();
