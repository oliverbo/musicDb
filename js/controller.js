var musicDbControllers = angular.module('musicDbControllers', ['musicDbServices']);

musicDbControllers.controller("ArtistController", function($scope, Artist) {
	$scope.artists = Artist.query();
});

musicDbControllers.controller("AdminController", function($scope, Artist) {
	$scope.adminName = "Admin";

	this.save = function() {
		var artist = new Artist(
			{canonicalName:this.canonicalName,
			 displayName:this.displayName,
			 startYear:this.startYear
		 });
		 artist.$save();	 
	}
});
