var musicDbApp = angular.module('musicDbApp', []);

musicDbApp.controller("ArtistController", function($scope, $http) {
	$http.get("/api/artist").success(function(data) {
		$scope.artists = data
	})
});