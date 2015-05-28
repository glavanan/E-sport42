/**
 * Created by cwagner on 17/03/15.
 */

(function () {
    'use strict';

    angular
        .module('esport42.utils.services')
        .factory('_', Underscore)
        .factory('fileReader', fileReader)
        .factory('Users', Users);


    FileReader.$inject = ["$q", "$log"];

    Users.$inject = ['$http', '$q', '_'];

    function Users($http, $q, _) {
        var accounts_url = "api/v1/accounts";

        return {
            all: getAllUsers,
            allUsernames: getAllUsernames
        };

        function getAllUsers() {
            return $http.get(accounts_url)
                .then(function (data, status) {
                    return data.data;
                }, function (data, status) {
                    console.log("I failed in users services", data.data);
                    return $q.reject(data);
                });
        }

        function getAllUsernames() {
            return getAllUsers()
                .then(function (data, status, headers, config) {
                    return _.map(data, function (user) {return user.username;});
                }, function (data, status, headers, config) {
                    return $q.reject(data);
                });
        }
    }

    function Underscore() {
        return window._;
    }

    function fileReader ($q, $log) {
        // http://odetocode.com/blogs/scott/archive/2013/07/03/building-a-filereader-service-for-angularjs-the-service.aspx
        var onLoad = function(reader, deferred, scope) {
            return function () {
                scope.$apply(function () {
                    deferred.resolve(reader.result);
                });
            };
        };
        var onError = function (reader, deferred, scope) {
            return function () {
                scope.$apply(function () {
                    deferred.reject(reader.result);
                });
            };
        };
        var onProgress = function(reader, scope) {
            return function (event) {
                scope.$broadcast("fileProgress",
                    {
                        total: event.total,
                        loaded: event.loaded
                    });
            };
        };
        var getReader = function(deferred, scope) {
            var reader = new FileReader();
            reader.onload = onLoad(reader, deferred, scope);
            reader.onerror = onError(reader, deferred, scope);
            reader.onprogress = onProgress(reader, scope);
            return reader;
        };
        var readAsDataURL = function (file, scope) {
            var deferred = $q.defer();

            var reader = getReader(deferred, scope);
            reader.readAsDataURL(file);

            return deferred.promise;
        };
        return {
            readAsDataUrl: readAsDataURL
        };
    }
})();