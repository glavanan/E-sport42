/**
 * Created by cwagner on 16/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.posts.controller')
        .controller('PostController', PostController);

    PostController.$inject = ['$http', 'Post'];

    function PostController($http, Post){
        var vm = this;


    }

})();