/**
 * Created by cwagner on 16/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.posts.services')
        .factory('Post', Post);

    Post.$inject = ['$http'];

    function Post($http) {
        var Post = {
            all: all
        };

        return Post;

        function all() {
            return $http.get('/api/v1/posts');
        }
    }
})();