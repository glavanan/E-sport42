/**
 * Created by cwagner on 25/02/2015.
 */
(function () {
    console.log("1");
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
    console.log("AFFDF");
    function run ($http) {
        console.log("In da function");
          $http.defaults.xsrfHeaderName = 'X-CSRFToken';
          $http.defaults.xsrfCookieName = 'csrftoken';
    }
    console.log("LOLOL");
})

(function () {
    console.log('lolol');
    angular.module("esport42", []);
    console.log("lol");
    console.log(angular.module('esport42'));
    //sfklsaflkasnfklsnfkldsnf
})
