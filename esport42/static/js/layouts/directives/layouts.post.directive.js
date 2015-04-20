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
                console.log(scope.article);
                scope.clickOn = function () {
                    scope.clicked = (scope.clicked === "true" ? "false" : "true");
/*
                    var mydiv = angular.element(elem.children()[0]);
                    var h = mydiv.height();
                    console.log(h);
                    mydiv.height(h + 200);
                    console.log(mydiv.height());
*/
                }
            }
        }
    }
})();
