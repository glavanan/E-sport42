/**
 * Created by cwagner on 16/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.layouts.controllers')
        .controller('IndexController', IndexController);

    IndexController.$inject = ['Post', '_'];

    function IndexController(Post, _) {
        var vm = this;

        vm.posts = [];

        activate();

        //console.log(Post.all);
        function activate() {
            //var trim = require("underscore.string/trim");

            Post.all()
                .success(PostSuccess)
                .error(PostFailure);

            function PostSuccess(data) {
                vm.posts = _.map(data, function (data) {
                    return {
                        summary: "Je suis un canard",
                        text: data.text,
                        imgCropped: data.image_url,
                        imgFull: data.image,
                        title: data.title,
                        author: data.author.username
                    }
                });
            }

            function PostFailure(data) {
                console.log('error bitch');
            }
        }

    }
})();