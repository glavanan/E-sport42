/**
 * Created by cwagner on 16/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.tournaments.services')
        .factory('Tournaments', Tournaments);

    Tournaments.$inject = ['$http', '_', '$q'];

    function Tournaments($http, _, $q) {

        var tournaments_url = '/api/v1/tournoi';

        var Tournaments = {
            all: all
            //newPost: newPost,
            //deletePost: deletePost
        };

        return Tournaments;

        function all() {
            return $http.get(tournaments_url)
                .then(function (data, status) {
                    return _.map(data.data, function (data) {
                        return (data);
                    });
                }, function (data, status) {
                    console.log("Get Tournament Error in service: ", data);
                    return $q.reject(data);
                });
        }

        //function newPost(image, form) {
        //    var uploadOpts = {
        //        url: post_url,
        //        fields: {
        //            title: form.title,
        //            resume: form.summary,
        //            text: form.text,
        //            is_landing: form.is_landing
        //        },
        //        file: image,
        //        fileFormDataName: 'image'
        //    };
        //
        //    return Upload.upload(uploadOpts)
        //        .then(function (data, status, headers, config) {
        //            return data.data;
        //        }, function (data, status, headers, config) {
        //            console.log("Upload of file failed: ", data);
        //            return data.data;
        //        });
        //}
        //
        //function deletePost(id) {
        //    return $http.delete(post_url + '/' + id);
        //}
    }
}());