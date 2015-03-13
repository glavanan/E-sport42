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

    Authentication.$inject = ['$cookies', '$http'];
    Focus.$inject = ['$rootScope', '$timeout'];

    function Authentication ($cookies, $http) {

        var Authentication = {
            register : register,
            login: login,
            getAuthenticatedAccount: getAuthenticatedAccount,
            setAuthenticatedAccount: setAuthenticatedAccount,
            isAuthenticated: isAuthenticated,
            unauthenticate: unauthenticate
        };

        return Authentication;

        function register (data) {
            return $http.post('/api/v1/accounts', data).then(registerSuccess, registerError);
            function registerSuccess(dataReceived, status, headers, config) {
                Authentication.login(data.email, data.password);
            }
            function registerError(dataReceived, status, headers, config) {
                    alert('Something was wrong. It should not have happend. Contact the administrator');
                console.log(dataReceived);
            }
        }
        function login (username, password) {
            return $http.post('/api/v1/login', {
                username: username,
                password: password
            });
        //    }).then(loginSuccess, loginError);
        //    function loginSuccess(data, status, headers, config) {
        //        Authentication.setAuthenticatedAccount(data.data);
        //        window.location = '/';
        //    }
        //    function loginError(data, status, headers, config) {
        //        alert('Mysterious problem while logging in... Please contact administrator.');
        //        console.log(data);
        //    }
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