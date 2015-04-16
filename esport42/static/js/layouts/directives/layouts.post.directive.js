/**
 * Created by cwagner on 09/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.layouts.directives')
        .directive('postArticle', post);

    function post() {
        return {
            restrict: 'E', // only activate on element attribute
            scope: {
                article: "="
            },
            templateUrl: "static/templates/layouts/post-directive.html",
            link: function (scope, elem, attrs) {
                scope.clicked = "false";
                scope.clickOn = function () {
                    console.log(scope.clicked);
                    scope.clicked = (scope.clicked === "true" ? "false" : "true");
                }
            }
        }
    }
})();
