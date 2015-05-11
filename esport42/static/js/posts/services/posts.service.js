/**
 * Created by cwagner on 16/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.posts.services')
        .factory('Post', Post);

    Post.$inject = ['$http', 'Upload', '_', '$q'];

    function Post($http, Upload, _, $q) {

        var post_url = '/api/v1/posts';

        var Post = {
            all: all,
            newPost: newPost,
            deletePost: deletePost
        };

        return Post;

        function all() {
            return $http.get(post_url)
                .then(function (data, status) {
                    return _.map(data.data, function (data) {
                        return {
                            summary: data.resume,
                            text: data.text,
                            imgCropped: data.image_url,
                            imgFull: data.image,
                            title: data.title,
                            author: data.author.username,
                            is_landing: data.is_landing,
                            id: data.id
                        }
                    });
                }, function (data, status) {
                    console.log("Failed in post service...");
                    return $q.reject(data);
                });
        }

        function newPost(image, form) {
            var uploadOpts = {
                url: post_url,
                fields: {
                    title: form.title,
                    resume: form.summary,
                    text: form.text,
                    is_landing: form.is_landing
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

        function deletePost(id) {
            return $http.delete(post_url + '/' + id);
        }
    }
}());