/**
 * Created by oddnaughty on 3/11/15.
 */

(function () {

    angular
        .module('esport42.tournaments.directives')
        .directive('teamNameAvailable', teamNameAvailable);

    teamNameAvailable.$inject = ['$http'];

    function teamNameAvailable($http) {
        return {
            require: 'ngModel',
            link: function ($scope, elem, attrs, ngModel) {
                ngModel.$asyncValidators.teamNameAvailable = function (tournament, teamname) {
                    //return $http.get('/api/v1/username-exists?username=' + username);
                    return $http.get('/api/v1/tournament/' + tournament.id + "/teamname-exists?name=" + teamname);
                }
            }
        }
    }
})();
