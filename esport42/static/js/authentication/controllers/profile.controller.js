/**
 * Created by oddnaughty on 3/13/15.
 */

(function () {

    angular
        .module('esport42.authentication.controllers')
        .controller('ProfileController', ProfileController);

    ProfileController.$inject = ['Authentication', 'user'];

    function ProfileController(Authentication, user) {
        var vm = this;

        vm.error = null;
        vm.form = null;
        vm.usernameSave = null;
        vm.updateProfile = updateProfile;

        activate ();

        function activate() {
            vm.form = user;
            vm.usernameSave = user.username;
        }

        function updateProfile() {
            Authentication.update(vm.form);
        }
    }
})();