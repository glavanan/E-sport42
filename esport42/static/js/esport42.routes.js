/**
 * Created by cwagner on 25/02/2015.
 */
(function () {
    'use strict';
    console.log("lolol");
    angular
        .module('esport42.routes')
        .config(config);

    config.$inject = ['$routeProvider'];

    function config($routeProvider) {
        $routeProvider
            .when('/lol', {
                controller: 'RegisterController',
                controllerAs: 'vm',
                templateUrl: '/templates/site/register.html'
            })
            .otherwise('/');
    }
})