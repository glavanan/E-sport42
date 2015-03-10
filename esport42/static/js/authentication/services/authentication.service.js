/**
 * Created by cwagner on 05/03/2015.
 */

(function (){
    'use strict';

    angular
        .module("esport42.authentication.services")
        .factory("Authentication", Authentication)

    angular
        .module("esport42.authentication.services")
        .factory("Focus", Focus);

    Authentication.$inject = ['$cookies', '$http'];
    Focus.$inject = ['$rootScope', '$timeout'];

    function Authentication ($cookies, $http) {

        var Authentication = {
            register : register
        };

        return Authentication;

        function register (data) {
            return $http.post('/api/v1/accounts', data);
        }
    }

        function Focus ($rootScope, $timeout) {
            return function (name) {
                $timeout(function () {
                    $rootScope.$broadcast('focusOn', name);
                    console.log('focus On declenched !');
                });
            }
        }
})();