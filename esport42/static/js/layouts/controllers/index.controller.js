/**
 * Created by cwagner on 16/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.layouts.controllers')
        .controller('IndexController', IndexController);

    IndexController.$inject = ['Post'];

    function IndexController(Post) {
        var vm = this;

        vm.posts = [];

        activate();

        //console.log(Post.all);
        function activate() {

            Post.all()
                .success(PostSuccess)
                .error(PostFailure);

            function PostSuccess(data) {
                vm.posts = data;
                console.log('Posts:', vm.posts);
            }
            function PostFailure(data) {
                console.log('error bitch');
            }
        }
    }
})();