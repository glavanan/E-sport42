(function () {
    'use strict';

    angular.
        module('esport42.utils').
        controller('TestController', TestCtrl);

    TestCtrl.$inject = ['Users', 'ngDialog'];

    function TestCtrl(Users, ngDialog) {
        var vm = this;

        activate();

        function activate() {
            Users.all().finally(function (data) {
                console.log('kaka');
            });
        }
    }

})();