var musicDbControllers = angular.module('musicDbControllers', ['musicDbServices', 'pageModule']);

musicDbControllers.controller("ArtistController", function($scope, Artist, userName, logoutURI) {
	$scope.userName = userName;
	$scope.logoutURI = logoutURI;
	$scope.artists = Artist.query();
});

musicDbControllers.controller("ArtistAdminController", function($scope, Artist) {
	$scope.adminName = "Admin";

	this.save = function() {
		var artist = new Artist(
			{
				canonicalName : this.canonicalName,
			 	displayName : this.displayName,
			 	startYear : this.startYear
		 });
		 artist.$save();	 
	}
});

musicDbControllers.controller("VenueController", function($scope, Venue) {
	$scope.venues = Venue.query();
});


musicDbControllers.controller("VenueAdminController", function($scope, Venue) {
	this.save = function() {
		var venue = new Venue(
			{
				canonicalName : this.canonicalName,
			 	displayName : this.displayName,
			 	startYear : this.startYear,
				address : this.address,
				description : this.description
		 });
		 venue.$save();
	}
});


