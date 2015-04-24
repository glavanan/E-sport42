/**
 * Created by cwagner on 16/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.posts.controllers')
        .controller('PostController', PostController);

    PostController.$inject = ['$anchorScroll', '$location', 'Post', 'Authentication', '$timeout'] ;

    function PostController($anchorScroll, $location,Post, Authentication, $timeout){
        var vm = this;
        vm.displayPreview = displayPreview;

        vm.form = {
            "imgCropped": "static/img/post/img95.crop.jpg",
            "imgFull": "http://localhost:8080/static/img/post/img95_e7XPKgK.jpg",
            "author": Authentication.getAuthenticatedAccount().data.username
        };

        function displayPreview () {
            vm.displayed = true;
            vm.postDefault = vm.form;
            $timeout(function () {window.scrollTo(0, 300);}, 100);
        }
    }
})();