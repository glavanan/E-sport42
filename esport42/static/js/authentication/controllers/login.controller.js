/**
 * Created by oddnaughty on 3/13/15.
 */

(function () {

    angular
        .module('esport42.authentication.controllers')
        .controller('LoginController', LoginController);

    LoginController.$inject = ['$location', '$scope', '$filter', 'Authentication', 'Focus'];

    function LoginController($location, $scope, $filter, Authentication, Focus) {
        var vm = this;

        vm.error = null;
        vm.login = login;

        activate();

        function activate() {
            if (Authentication.isAuthenticated())
                $location.path('/');
        }
        function login() {
            vm.loginPending = true;
            vm.error = {};
            Authentication.login(vm.form.username, vm.form.password)
                .then(
                function (data, status, headers, config) {
                    window.location = '/';
                },
                function(data, status, headers, config) {
                    console.log("Login error: ", data);
                    if (data.username)
                        vm.error.username = data.username;
                    if (data.non_field_errors)
                        vm.error.non_field_errors = data.non_field_errors;
                }
            ).finally(function () {vm.loginPending = false;});
        }
    }
})();