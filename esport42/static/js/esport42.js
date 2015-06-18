/**
 * Created by cwagner on 25/02/2015.
 */
(function () {
    angular
        .module('esport42', [
            'ngAnimate', 'ngSanitize', 'textAngular', 'ngFileUpload', 'ui.router', 'ui.select', 'ngDialog',
            'esport42.config',
            'esport42.routes',
            'esport42.utils',
            'esport42.authentication',
            'esport42.layouts',
            'esport42.posts',
            'esport42.tournaments'
        ]);
    angular
        .module('esport42.routes', []);
    angular
        .module('esport42.config', []);
    angular
        .module('esport42.utils', []);
    angular
        .module('esport42.authentication', []);
    angular
        .module('esport42.layouts', []);
    angular
        .module('esport42.posts', []);
    angular
        .module('esport42')
        .run(run);

    run.$inject = ['$http', '$rootScope', '$state', 'Authentication'];
    function run ($http, $rootScope, $state, Authentication) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';

        $rootScope.$on('$stateChangeStart', function (event, toState, toParams, fromState) {

            if (toState.data) {
                var priority = [
                    "requireLogin",
                    "requireAdmin"
                ];
                var go_funcs = [
                    function () {$state.go('login');},
                    function () {$state.go('home');}
                ];
                angular.forEach(priority, function (value, key) {
                    if (value in toState.data) {
                        go_funcs[key]();
                        event.preventDefault();
                        return;
                    }
                });
            }
        });
    }
})();