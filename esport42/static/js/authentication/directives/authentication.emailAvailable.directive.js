/**
 * Created by oddnaughty on 3/11/15.
 */

(function () {

    angular
        .module('esport42.authentication.directives')
        .directive('emailAvailable', emailAvailable);

    emailAvailable.$inject = ['$http'];

    function emailAvailable($http) {
        return {
            require: 'ngModel',
            link: function ($scope, elem, attrs, ngModel) {
                ngModel.$asyncValidators.emailAvailable = function (email) {
                    return $http.get('/api/v1/email-exists?e=' + email);
                }
            }
        }
    }
})();
