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
                url: "/home",
                controller: 'IndexController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/layouts/index.html'
            })
            .state('newPost', {
                url: "/post",
                controller: 'PostController',
                data: {requireLogin: true, requireAdmin: true},
                controllerAs: 'vm',
                templateUrl: '/static/templates/post/post.html'
            })
            .state('test', {
                url: "/test",
                data: {requireLogin: true, requireAdmin: true},
                controller: 'TestController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/test/test-ui-select.html'
            })
            .state('tournament-detail', {
                url: "/tournaments/:tournamentName",
                templateUrl: '/static/templates/tournaments/tournament-detail.html',
                resolve: {
                    tournament: ['Tournaments', '$stateParams', function (Tournaments, $stateParams) {
                        return Tournaments.getTournamentByTag($stateParams.tournamentName);
                    }]
                },
                controller: 'TournamentDetailController',
                controllerAs: 'vm'
            })
            .state('tournament-detail.register-team', {
                url: "/register",
                templateUrl: '/static/templates/tournaments/tournament-detail-register-team.html',
                data: {requireLogin: true},
                controller: 'TournamentDetailRegisterController',
                controllerAs: 'vm'
            })
            .state('tournament-detail.register-solo', {
                url: "/register-solo",
                templateUrl: '/static/templates/tournaments/tournament-detail-register-solo.html',
                data: {requireLogin: true},
                controller: 'TournamentDetailRegisterSoloController',
                controllerAs: 'vm'
            })
            .state('tournament-detail.register-cancel', {
                url: "/register-cancel",
                templateUrl: '/static/templates/tournaments/tournament-detail-register-cancel.html',
                controller: ['tournament', '$scope', function (tournament, $scope) {
                    $scope.tournament = tournament;
                }]
            })
            .state('tournament-detail.register-success', {
                url: "/register-success?teamName",
                templateUrl: '/static/templates/tournaments/tournament-detail-register-success.html',
                controller: ['tournament', '$scope', '$stateParams', function (tournament, $scope, $stateParams) {
                    $scope.tournament = tournament;
                    $scope.teamName = $stateParams['teamName'];
                }]
            });
    }
})();