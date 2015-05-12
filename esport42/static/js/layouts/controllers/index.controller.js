/**
 * Created by cwagner on 16/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.layouts.controllers')
        .controller('IndexController', IndexController);

    IndexController.$inject = ['Post', 'Authentication'];

    function IndexController(Post, Authentication) {
        var vm = this;

        vm.posts = [];

        activate();

        function activate() {

            vm.user = Authentication.getAuthenticatedAccount();
            Post.all()
                .then(PostSuccess, PostFailure);

            function PostSuccess(data) {
                vm.posts = data;
            }

            function PostFailure(data) {
                console.log('Get Posts failed: ', data);
            }
        }

    }
})();