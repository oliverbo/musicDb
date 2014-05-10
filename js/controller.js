var musicDbControllers = angular.module('musicDbControllers', ['musicDbServices', 'pageModule']);

musicDbControllers.controller("PageHeaderController", function($scope, pageInfo) {
	$scope.userName = pageInfo.userName;
	$scope.logoutURI = pageInfo.logoutURI;
	$scope.loginURI = pageInfo.loginURI;
	pageInfo.isAdmin ? $scope.isAdmin = true : $scopeIsAdmin = false;
});

musicDbControllers.controller("ArtistController", function($scope, Artist) {
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

musicDbControllers.controller("VenueController", function($scope, Venue, pageInfo) {
	$scope.venues = Venue.query();
});


musicDbControllers.controller("VenueAdminController", function($scope, Venue) {
	this.save = function() {
		var venue = new Venue(
			{
				canonicalName : this.canonicalName,
			 	displayName : this.displayName,
				address : this.address,
				description : this.description,
				capacity : this.capacity
		 });
		 venue.$save();
	}
});


