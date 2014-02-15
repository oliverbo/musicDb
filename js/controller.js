var musicDbControllers = angular.module('musicDbControllers', ['musicDbServices']);

musicDbControllers.controller("ArtistController", function($scope, Artist) {
	$scope.artists = Artist.query();
});