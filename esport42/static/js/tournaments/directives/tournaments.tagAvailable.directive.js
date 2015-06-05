/**
 * Created by oddnaughty on 3/11/15.
 */

(function () {

    angular
        .module('esport42.tournaments.directives')
        .directive('tagAvailable', tagAvailable);

    tagAvailable.$inject = ['$http'];

    function tagAvailable($http) {
        return {
            restrict: 'A',
            require: 'ngModel',
            link: function ($scope, elem, attrs, ngModel) {
                ngModel.$asyncValidators.tagAvailable = function (teamname) {
                    return $http.get('/api/v1/tag-exists?tournament=' + attrs.tagAvailable +  '&name=' + teamname);
                }
            }
        }
    }
})();
