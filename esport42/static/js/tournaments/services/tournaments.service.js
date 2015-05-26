/**
 * Created by cwagner on 16/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.tournaments.services')
        .factory('Tournaments', Tournaments);

    Tournaments.$inject = ['$http', '_', '$q'];

    function Tournaments($http, _, $q) {

        var tournaments_url = '/api/v1/tournoi';

        var Tournaments = {
            all: all,
            submitTeam: submitTeam
            //newPost: newPost,
            //deletePost: deletePost
        };

        return Tournaments;

        function all() {
            return $http.get(tournaments_url)
                .then(function (data, status) {
                    return _.map(data.data, function (data) {
                        return (data);
                    });
                }, function (data, status) {
                    console.log("Get Tournament Error in service: ", data);
                    return $q.reject(data);
                });
        }
        
        function submitTeam(tournamentId, team) {
            return $http.post(tournaments_url + "/" + tournamentId + "/team", team)
                .then(function (data, status, headers, config) {
                    return data.data;
                }, function (data, status, headers, config) {
                    console.log("Team submit failed in service: ", data);
                    return $q.reject(data);
                });
        }
    }
}());