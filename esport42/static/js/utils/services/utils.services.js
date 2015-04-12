/**
 * Created by cwagner on 17/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.utils.services')
        .factory('_', Underscore);

    function Underscore() {
        return window._;
    }

})();