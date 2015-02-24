/**
 * Created by cwagner on 24/02/2015.
 */

(function(){

    'use strict';

    //(1)
    var Blog = angular
        .module("site.base",
        ["ngCookies"], function ($interpolateProvider) {
            $interpolateProvider.startSymbol("{$");
            $interpolateProvider.endSymbol("$}");
        }
    );

    Blog.config(function($httpProvider) {
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    });

    //(2)
    Blog.run(function ($http, $cookies) {
        $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
    });

    ////(3)
    //Blog.config(function ($routeProvider) {
    //    $routeProvider
    //        .when("/", {
    //            templateUrl: "static/js/app/views/feed.html",
    //            controller: "FeedController",
    //        })
    //        //.when("/post/:id", {
    //        //    templateUrl: "static/js/app/views/view.html",
    //        //    controller: "PostController",
    //        //    resolve: {
    //        //        post: function ($route, PostService) {
    //        //            var postId = $route.current.params.id;
    //        //            return PostService.get(postId);
    //        //        }
    //        //    }
    //        //})
    //        .otherwise({
    //            redirectTo: '/'
    //        })
    //});
})