(function () {
    'use strict';

    angular.
        module('esport42.utils').
        controller('TestController', TestCtrl);

    TestCtrl.$inject = ['Users', 'ngDialog'];

    function TestCtrl(Users, ngDialog) {
        var vm = this;

        vm.users = null;
        vm.selectedPeople = [];

        activate();

        function activate() {
            Users.all().then(function (data) {vm.users = data; console.log(data)})
                ngDialog.open({
                    template: 'firstDialogId',
                    //controller: 'InsideCtrl',
                    className: 'ngdialog-theme-plain'
                });
        }
    }
//                        <img alt="spinning-wheel" src="{% static 'img/site/spinning-wheel.GIF' %}" height="100%"></a>

})();