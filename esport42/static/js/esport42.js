/**
 * Created by cwagner on 25/02/2015.
 */
(function () {
    angular
        .module('esport42', [
            'esport42.config',
            'esport42.routes',
            'esport42.site'
        ]);
    angular
        .module('esport42.routes', ['ngRoute']);
    angular
        .module('esport42.config', []);
    angular
        .module('esport42.site', []);
    angular
        .module('esport42')
        .run(run);

    run.$inject = ['$http'];
    function run ($http) {
          $http.defaults.xsrfHeaderName = 'X-CSRFToken';
          $http.defaults.xsrfCookieName = 'csrftoken';
    }
})();