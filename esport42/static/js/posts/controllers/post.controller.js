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
            "author": Authentication.getAuthenticatedAccount().username
        };

        var upload = function (file) {
            if (file) {
                Upload.upload({
                    url: 'http://localhost:8000/api/v1/posts',
                    fields: {
                        'title': vm.form.title,
                        'resume': vm.form.summary,
                        'text': vm.form.text
                    },
                    file: file,
                    fileFormDataName: 'image'
                }).progress(function (evt) {
                    var progressPercentage = parseInt(100.0 * evt.loaded / evt.total);
                    console.log('progress: ' + progressPercentage + '% ' + evt.config.file.name);
                }).success(function (data, status, headers, config) {
                    $location.path('/');
                }).error(function (data, status, headers, config) {
                    console.log("An error happened at the upload...: ", data);
                });
            }
        };

        function post(form) {
            if (form.$valid && vm.form && vm.file && (vm.displayed || confirm("Avez vous bien regardé l'apercu d'abord ? :)"))) {
                Post.newPost(vm.file, vm.form)
                    .then(function (data, status) {
                        $location.url('/');
                    }, function (data, status) {
                        console.log("Uploading Post failed...: ", data);
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