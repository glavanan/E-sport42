/**
 * Created by cwagner on 16/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.posts.controllers')
        .controller('PostController', PostController);

    PostController.$inject = ['$http', 'Post'] ;

    function PostController($http, Post){
        var vm = this;

        vm.error = null;
        vm.post = post;

        function post() {
            vm.error = null;
            Post.post(vm.form.text, vm.form.resume, vm.form.title, vm.form.image)
                .success()
        }
    }

})();