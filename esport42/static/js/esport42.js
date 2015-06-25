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

    run.$inject = ['$http', '$rootScope', '$state', 'Authentication', 'Tournaments'];
    function run ($http, $rootScope, $state, Authentication, Tournaments) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';

        $rootScope.$on('$stateChangeStart', function (event, toState, toParams, fromState) {
            if (toState.data) {
                var user = Authentication.getAuthenticatedAccount();
                var shouldLog = !user && 'requireLogin' in toState.data;
                var shouldBeAdmin = !user || (user && !(user.is_admin && user.is_staff)) && 'requireAdmin' in toState.data;
                var shouldBeRedirectRegistrationEnd = 'beforeRegistrationEnd' in toState.data && toState.data.beforeRegistrationEnd;

                function go_to(state) {
                    $state.go(state);
                }
                function redirect(state) {
                    go_to(state);
                    event.preventDefault();
                    return;
                }

                if (shouldBeRedirectRegistrationEnd) {
                    Tournaments.getTournamentByTag(toParams.tournamentName)
                        .then(function (data) {
                            var tournament = data;
                            if (new Date (tournament.end_reg) < Date.now()) {
                                return redirect ('home');
                            }
                        });
                }

                if (shouldLog) {
                    return redirect('login');
                }
                if (shouldBeAdmin) {
                    if (!user)
                        return redirect('login');
                    else
                        return redirect('home');
                }
            }
        });
    }
})();