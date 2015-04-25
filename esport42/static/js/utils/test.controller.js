(function () {
    'use strict';

    angular.
        module('esport42.utils').
        controller('TestController', TestCtrl);

    TestCtrl.$inject = ['$scope', 'Post', '$cookies', 'Upload'];

    function TestCtrl($scope, Post, $cookies, Upload) {
        var vm = this;
        vm.post = post;

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
                    window.location.href = '/';
                }).error(function (data, status, headers, config) {
                    console.log("An error happened at the upload...: ", data);
                });
            }
        };

        function post() {
            console.log(vm.form);
            if (confirm("Avez vous bien regardé l'apercu d'abord ? :)"))
                upload(vm.file);
        }
    }
})();