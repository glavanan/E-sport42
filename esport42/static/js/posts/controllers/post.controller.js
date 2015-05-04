/**
 * Created by cwagner on 16/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.posts.controllers')
        .controller('PostController', PostController);

    PostController.$inject = ['$scope', '$location', 'Post', 'Authentication', '$timeout', 'fileReader'];

    function PostController($scope, $location, Post, Authentication, $timeout, fileReader) {
        var vm = this;
        vm.displayPreview = displayPreview;
        vm.post = post;
        vm.displayed = false;

        vm.form = {
            "author": Authentication.getAuthenticatedAccount().data.username
        };


        function post(form) {
            if (form.$valid && vm.form && vm.file && (vm.displayed || confirm("Avez vous bien regardé l'apercu d'abord ? :)"))) {
                Post.newPost(vm.file, vm.form)
                    .then(function (data, status) {
                        $location.url('/');
                    }, function (data, status) {
                        console.log("I'm in controller bitch and I failed: ", data);
                    }
                );
            }
            else
                displayPreview(form);
        }

        function displayPreview(form) {
            if (form.$valid) {
                fileReader.readAsDataUrl(vm.file[0], $scope)
                    .then(function (result) {
                        vm.displayed = true;
                        vm.form.imgFull = result;
                        vm.postDefault = vm.form;
                        $timeout(function () {
                            window.scrollTo(0, 300);
                        }, 100);
                    });
            }
            else {
                alert("Le formulaire est mal rempli...");
            }
        }
    }
})();