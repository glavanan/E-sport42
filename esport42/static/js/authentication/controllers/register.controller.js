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

        function registerMandatory(isValid) {
            if (!isValid)
                return ;
            else if (vm.form.password && vm.form.password == vm.form.password_confirm)
                vm.next = true;
            else
                alert("Both passwords are different");
        }

        function registerOptional(isValid) {
            if (vm.date !== vm.dirtyDate)
                vm.form.birth_date = $filter('date')(vm.date, "yyyy/MM/dd");
            if (!isValid)
                return ;
            console.log(vm.form);
            Authentication.register(vm.form)
                .success(function (data, status, headers, config) {
                    $location.path('/');
                    alert('You have been registered');
                })
                .error(function (data, status, headers, config) {
                    alert('Something was wrong. It should not have happend. Contact the administrator');
                    console.log(data);
                });
         }
    }
})();
