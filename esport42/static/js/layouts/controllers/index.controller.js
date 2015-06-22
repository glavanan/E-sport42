/**
 * Created by cwagner on 16/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.layouts.controllers')
        .controller('IndexController', IndexController);

    IndexController.$inject = ['Authentication', 'posts'];

    function IndexController(Authentication, posts) {
        var vm = this;

        vm.posts = posts;

        activate();

        function activate() {
            vm.user = Authentication.getAuthenticatedAccount();
        }

    }
})();