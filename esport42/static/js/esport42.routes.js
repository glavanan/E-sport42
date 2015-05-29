/**
 * Created by cwagner on 25/02/2015.
 */
(function () {
    'use strict';
    angular
        .module('esport42.routes')
        .config(config);

    config.$inject = ['$stateProvider', '$urlRouterProvider'];

    function config($stateProvider, $urlRouterProvider) {
        $urlRouterProvider.otherwise('/');
        $stateProvider
            .state('register', {
                url: '/register',
                controller: 'RegisterController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/authentication/register.html'
            })
            .state('login', {
                url: "/login",
                controller: 'LoginController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/authentication/login.html'
            })
            .state('home', {
                url: "/",
                controller: 'IndexController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/layouts/index.html'
            })
            .state('newPost', {
                url: "/post",
                controller: 'PostController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/post/post.html'
            })
            .state('test', {
                url: "/test",
                controller: 'TestController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/test/test-ui-select.html'
            })
            .state('tournament-detail', {
                url: "/tournaments/:tournamentName",
                templateUrl: '/static/templates/tournaments/tournament-detail.html',
                resolve: {
                    tournament: ['Tournaments', '$stateParams', function (Tournaments, $stateParams) {
                        return Tournaments.getTournamentByName($stateParams.tournamentName);
                    }]
                },
                controller: 'TournamentDetailController',
                controllerAs: 'vm'
            })
            .state('tournament-detail.register', {
                url: "/register",
                templateUrl: '/static/templates/tournaments/tournament-detail-register.html',
                controller: 'TournamentDetailRegisterController',
                controllerAs: 'vm'
            });
    }
})();