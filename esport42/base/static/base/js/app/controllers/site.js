/**
 * Created by cwagner on 24/02/2015.
 */

(function () {
  'use strict';

  angular
    .module('site.base.controllers')
    .controller('RegisterController', RegisterController);

  RegisterController.$inject = ['$location', '$scope'];

  /**
  * @namespace RegisterController
  */
  function RegisterController($location, $scope, Authentication) {
      var vm = this;
      vm.var = '';
  }
})();