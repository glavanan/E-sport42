/**
 * Created by cwagner on 25/02/2015.
 */

(function () {
    'use strict';
    angular
        .module('esport42.config')
        .config(config);
    config.$inject = ['$locationProvider'];

    function config($locationProvider) {
        $locationProvider.html5Mode(true);
        $locationProvider.hashPrefix('!');
    }
})();