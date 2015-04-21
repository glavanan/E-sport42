/**
 * Created by cwagner on 05/03/2015.
 */

(function (){
    'use strict';

    angular
        .module("esport42.authentication.services")
        .factory("Authentication", Authentication);

    angular
        .module("esport42.authentication.services")
        .factory("Focus", Focus);

    Authentication.$inject = ['$cookies', '$http', '$q'];
    Focus.$inject = ['$rootScope', '$timeout'];

    function Authentication ($cookies, $http, $q) {

        var Authentication = {
            register : register,
            login: login,
            logout: logout,
            getAuthenticatedAccount: getAuthenticatedAccount,
            setAuthenticatedAccount: setAuthenticatedAccount,
            isAuthenticated: isAuthenticated,
            unauthenticate: unauthenticate
        };

        return Authentication;

        function register (data) {
            return $http.post('/api/v1/accounts', data).then(registerSuccess, registerError);
            function registerSuccess(dataReceived, status, headers, config) {
                return Authentication.login(data.username, data.password);
            }
            function registerError(dataReceived, status, headers, config) {
                alert('Something was wrong. It should not have happend. Contact the administrator');
                console.log(dataReceived);
                return $q.reject(dataReceived);
            }
        }

        function login (username, password) {
            return $http.post('/api/v1/login', {username: username, password: password})
                .then(function (dataReceived, status, headers, config) {
                    Authentication.setAuthenticatedAccount(dataReceived);
                }, function (dataReceived, status, headers, config) {
                    return $q.reject(dataReceived.data);
                });
        }

        function logout() {
            $http.post('/api/v1/logout', {})
                .success(function () {
                    unauthenticate();
                    window.location = '/';
                })
                .error(function () {
                    alert('We were unable to logout you. Please contact the administrator');
            });
        }
        function getAuthenticatedAccount() {
            if (!$cookies.authenticatedAccount)
                return ;
            return JSON.parse($cookies.authenticatedAccount);
        }

        function setAuthenticatedAccount(account) {
            $cookies.authenticatedAccount = JSON.stringify(account);
        }

        function isAuthenticated() {
            return !!$cookies.authenticatedAccount;
        }

        function unauthenticate() {
            delete $cookies.authenticatedAccount;
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