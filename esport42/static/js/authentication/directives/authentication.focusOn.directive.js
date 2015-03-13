/**
 * Created by oddnaughty on 3/10/15.
 */

(function () {

    angular
        .module('esport42.authentication.directives')
        .directive('focusOn', focusOn);


    function focusOn() {
        return function (scope, elem, attr) {
            console.log('wiwi jexist');
            scope.$on('focusOn', function (e, name) {
                if (name === attr.focusOn) {
                    elem[0].focus();
                }
            });
        };
    }
})();