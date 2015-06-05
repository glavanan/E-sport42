/**
 * Created by cwagner on 25/02/2015.
 */

(function () {
    angular
        .module('esport42.authentication.controllers')
        .controller('RegisterController', RegisterController);

    RegisterController.$inject = ['$location', '$scope', '$filter', 'Authentication', 'Focus'];

    function RegisterController($location, $scope, $filter, Authentication, Focus) {
        var vm = this;
        vm.registerMandatory = registerMandatory;
        vm.registerOptional = registerOptional;
        vm.next = false;
        vm.date = new Date();
        vm.dirtyDate = vm.date;
        vm.EMAIL_REGEXP = /^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/i;

        activate();

        function activate() {
            if (Authentication.isAuthenticated())
                $location.url('/');
        }

        function registerMandatory(isValid) {
            if (!isValid)
                return ;
            else if (vm.form.password && vm.form.password == vm.form.password_confirm) {
                vm.next = true;
                Focus("FocusFirstName");
            }
            else
                alert("Both passwords are different");
        }

        function registerOptional(isValid) {
            if (!isValid)
                return ;
            if (vm.date !== vm.dirtyDate)
                vm.form.birth_date = $filter('date')(vm.date, "yyyy-MM-dd");
            Authentication.register(vm.form).then(
                function (data, status, headers, config) {
                    Authentication.login(vm.form.username, vm.form.password).then(function(d) {
                        window.location.href = '/';
                    });
                    //alert('Vous etes maintenant inscrits !');
                },
                function (data, status, headers, config) {
                });
         }
    }
})();
