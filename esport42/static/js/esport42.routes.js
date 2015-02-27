/**
 * Created by cwagner on 25/02/2015.
 */
(function () {
    'use strict';
    angular
        .module('esport42.routes')
        .config(config);

    config.$inject = ['$routeProvider'];

    function config($routeProvider) {
        $routeProvider
            .when('/kaka/', {
                controller: 'RegisterController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/site/register.html'
            })
            .otherwise('/');
    }
})();