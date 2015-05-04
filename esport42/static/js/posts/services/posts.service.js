/**
 * Created by cwagner on 16/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.posts.services')
        .factory('Post', Post);

    Post.$inject = ['$http', 'Upload'];

    function Post($http, Upload) {
        var Post = {
            all: all,
            newPost: newPost
        };

        return Post;

        function all() {
            return $http.get('/api/v1/posts');
        }

        function newPost(image, form) {
            var uploadOpts = {
                url: 'api/v1/posts',
                fields: {
                    title: form.title,
                    resume: form.summary,
                    text: form.text
                },
                file: image,
                fileFormDataName: 'image'
            };

            return Upload.upload(uploadOpts)
                .then(function (data, status, headers, config) {
                    return data.data;
                }, function (data, status, headers, config) {
                    console.log("Fail dans l'upload: ", data);
                    return data.data;
                });
        }
    }
}());