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
            restrict: 'A',
            require: 'ngModel',
            link: function ($scope, elem, attrs, ngModel) {
                ngModel.$asyncValidators.teamNameAvailable = function (teamname) {
                    console.log($scope, attrs);
                    return $http.get('/api/v1/team-exists?tournament=' + attrs.teamNameAvailable +  '&name=' + teamname);
                }
            }
        }
    }
})();
