var musicDbControllers = angular.module('musicDbControllers', ['musicDbServices']);

musicDbControllers.controller("ArtistController", function($scope, Artist) {
	$scope.artists = Artist.query();
});

musicDbControllers.controller("AdminController", function($scope, Artist) {
	$scope.adminName = "Admin";
});
