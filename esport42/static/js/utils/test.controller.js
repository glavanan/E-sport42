(function () {
    'use strict';

    angular.
        module('esport42.utils').
        controller('TestController', TestCtrl);

    TestCtrl.$inject = ['$scope', 'Post', '$cookies', 'Upload'];

    function TestCtrl($scope, Post, $cookies, Upload) {
        var vm = this;
        vm.test = "test";
        vm.post = post;

        $scope.$watch('vm.files', function () {
            upload(vm.files);
        });

        var upload = function (files) {
        if (files && files.length) {
            for (var i = 0; i < files.length; i++) {
                var file = files[i];
                Upload.upload({
                    url: 'http://localhost:8080/api/v1/posts',
                    fields: {'title': "tarace", 'resume': "dfkjsdnfkjdsnfjkdsnfjkdsnf", 'text': "<h1>Je mange des penis</h1>"},
                    file: file,
                    fileFormDataName: 'image'
                }).progress(function (evt) {
                    var progressPercentage = parseInt(100.0 * evt.loaded / evt.total);
                    console.log('progress: ' + progressPercentage + '% ' + evt.config.file.name);
                }).success(function (data, status, headers, config) {
                    console.log('file ' + config.file.name + 'uploaded. Response: ' + data);
                });
            }
        }
    };

        //vm.uploader = new FileUploader({
        //    url: 'http://localhost:8080/api/v1/posts',
        //    headers: {
        //      'X-CSRFToken': $cookies['csrftoken']
        //    },
        //    formData: [vm.form]
        //});

        function post() {
            console.log(vm.form);
        }
    }
})();