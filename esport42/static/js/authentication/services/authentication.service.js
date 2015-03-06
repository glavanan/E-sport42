/**
 * Created by cwagner on 05/03/2015.
 */

(function (){
    'use strict';

    angular
        .module("esport42.authentication.services")
        .factory("Authentication", Authentication);

    Authentication.$inject = ['$cookies', '$http'];

    function Authentication ($cookies, $http) {

        var Authentication = {
            register : register
        };

        return Authentication;

        function register (email, password, username, firstName, lastName,  address, birthDate, nationality, phone ) {
            return $http.post('/api/v1/accounts', {
                email : email,
                password : password,
                username: username,
                first_name: firstName,
                last_name: lastName,
                address : address,
                birth_date : birthDate,
                nationality: nationality,
                phone: phone
            });
        }
    }
})();