/**
 * Created by oddnaughty on 3/11/15.
 */

(function () {

    angular
        .module('esport42.authentication.directives')
        .directive('usernameAvailable', usernameAvailable);

    usernameAvailable.$inject = ['$http'];

    function usernameAvailable($http) {
        return {
            require: 'ngModel',
            link: function ($scope, elem, attrs, ngModel) {
                ngModel.$asyncValidators.usernameAvailable = function (username) {
                    return $http.get('/api/v1/username-exists?username=' + username);
                }
            }
        }
    }
})();
