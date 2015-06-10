(function () {
    'use strict';

    angular.module('esport42.utils.directives')
        .directive('ajaxSpinner', ajaxSpinner);

    function ajaxSpinner() {
        return {
            scope: {

            }
        };
    }
})();