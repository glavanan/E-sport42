/**
 * Created by cwagner on 16/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.layouts.controllers')
        .controller('IndexController', IndexController);

    IndexController.$inject = ['$sce', 'Post', '_'];

    function IndexController($sce, Post, _) {
        var vm = this;

        vm.posts = [];

        activate();

        //console.log(Post.all);
        function activate() {

            Post.all()
                .success(PostSuccess)
                .error(PostFailure);

            function PostSuccess(data) {
                vm.posts = _.map(data, function (data) {return $sce.trustAsHtml(data.text)});
            }
            function PostFailure(data) {
                console.log('error bitch');
            }
        }
    }
})();