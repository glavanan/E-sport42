/**
 * Created by cwagner on 16/03/15.
 */

(function (){
    'use strict';

    angular
        .module('esport42.tournaments', [
            'esport42.tournaments.controllers',
            'esport42.tournaments.services',
            'esport42.tournaments.directives'
        ]);

    angular
        .module('esport42.tournaments.controllers', []);
    angular
        .module('esport42.tournaments.services', []);
    angular
        .module('esport42.tournaments.directives', []);
})();