/**
 * Created by cwagner on 09/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.layouts.directives')
        .directive('postArticle', post);

    post.$inject = ['Post'];

    function post(Post) {
        return {
            restrict: 'E', // only activate on element attribute
            scope: {
                article: "=",
                user: "="
            },
            templateUrl: "static/templates/layouts/post-directive.html",
            link: function (scope, elem, attrs) {
                scope.clicked = "false";
                scope.$on('$destroy', function(){console.log("I'm destroyed"); elem.remove()});
                scope.clickOn = function () {
                    scope.clicked = (scope.clicked === "true" ? "false" : "true");
                };

                scope.deletePost = function () {
                    Post.deletePost(scope.article.id);
                    //console.log("LOLOL");
                    scope.$broadcast('$destroy', 'Data to send');
                };
            }
        }
    }
})();
