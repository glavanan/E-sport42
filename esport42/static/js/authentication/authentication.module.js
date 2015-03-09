/**
 * Created by cwagner on 25/02/2015.
 */

(function () {
    'use strict';

    angular
        .module('esport42.authentication', [
            'esport42.authentication.controllers',
            'esport42.authentication.services',
            'esport42.authentication.directives'
        ]);
    angular
        .module('esport42.authentication.controllers', ['ngMessages']);
    angular
        .module('esport42.authentication.services', ['ngCookies']);
    angular
        .module('esport42.authentication.directives', []);

})();