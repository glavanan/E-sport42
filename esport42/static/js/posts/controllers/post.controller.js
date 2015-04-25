/**
 * Created by cwagner on 16/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.posts.controllers')
        .controller('PostController', PostController);

    PostController.$inject = ['$location', 'Upload', 'Authentication', '$timeout'] ;

    function PostController($location, Upload, Authentication, $timeout){
        var vm = this;
        vm.displayPreview = displayPreview;
        vm.post = post;

        vm.form = {
            "author": Authentication.getAuthenticatedAccount().data.username
        };

        var upload = function (file) {
            if (file) {
                Upload.upload({
                    url: 'http://localhost:8080/api/v1/posts',
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

        function post() {
            console.log(vm.form);
            if (confirm("Avez vous bien regardé l'apercu d'abord ? :)"))
                upload(vm.file);
            else
                displayPreview();
        }

        function displayPreview () {
            vm.displayed = true;
            vm.postDefault = vm.form;
            $timeout(function () {window.scrollTo(0, 300);}, 100);
        }
    }
})();