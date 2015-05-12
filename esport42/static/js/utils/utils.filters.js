(function () {
    'use strict';
    angular
        .module('esport42.utils.filters')
        .filter('escapeURL', escapeURL);

    function escapeURL() {
        return window.encodeURIComponent;
    }
})();