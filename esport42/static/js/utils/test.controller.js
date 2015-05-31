(function () {
    'use strict';

    angular.
        module('esport42.utils').
        controller('TestController', TestCtrl);

    TestCtrl.$inject = ['Users'];

    function TestCtrl(Users) {
        var vm = this;

        vm.users = null;

        activate();

        function activate() {
            Users.all().then(function (data) {vm.users = data; console.log(data)})
        }
    }
})();