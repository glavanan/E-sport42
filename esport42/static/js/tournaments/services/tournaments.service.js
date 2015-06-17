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
            getTournamentByName: getTournamentByName,
            getTournamentByTag: getTournamentByTag,
            submitTeam: submitTeam,
            submitSolo: submitSolo
            //deletePost: deletePost
        };

        return Tournaments;

        function all() {
            return $http.get(tournaments_url)
                .then(function (data, status) {
                    return _.map(data.data, function (data) {
                        transformTournament(data);
                        return (data);
                    });
                }, function (data, status) {
                    console.log("Get Tournament Error in service: ", data);
                    return $q.reject(data);
                });
        }

        function getTournamentByName(tName) {
            return $http.get(tournaments_url)
                .then(function (data, status) {
                    return transformTournament(_.find(data.data, function (data) {
                        return data.name === tName;
                    }));
                }, function (data, status) {
                    console.log("Get Tournament Error in service: ", data);
                    return $q.reject(data);
                });
        }

        function getTournamentByTag(tName) {
            return $http.get(tournaments_url)
                .then(function (data, status) {
                    return transformTournament(_.find(data.data, function (data) {
                        return data.tag === tName;
                    }));
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

        function submitSolo(tournamentId, user, paymentTo) {
            return $http.post("/api/v1/payment", {
                "id_event": tournamentId,
                "id_payer": user,
                "type_event": "Tournament",
                "type_payer": "MyUser",
                "payment_to": paymentTo
            })
                .then(function (data, status, headers, config) {
                    console.log("In submit solo: ", data.data);
                    return data.data;
                }, function (data, status, headers, config) {
                    console.log("Solo registration failed in service: ", data);
                    return $q.reject(data);
                });
        }

        function transformTournament(tournament) {
            var tagToName = {
                "LoL": "League of Legends",
                "HotS": "Heroes of the Storm",
                "CS:GO": "Counter-Strike: Global Offensive"
            };
            tournament.game_name = tagToName[tournament.game_name];
            return tournament;
        }

    }
}());