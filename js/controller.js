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

musicDbControllers.controller("VenueController", function($scope, $location, Venue, pageInfo) {
	$scope.venues = Venue.query();
	pageInfo.isAdmin ? $scope.isAdmin = true : $scope.isAdmin = false;
	$scope.showVenue = function(venue) {
		if (pageInfo.isAdmin) {
			$location.path('/admin/venues/' + venue.canonicalName);	
		} else {
			$location.path('/venues/' + venue.canonicalName);
		}
	};
	$scope.addVenue = function() {
		$location.path('/admin/venues/0');
	};
});


musicDbControllers.controller("VenuePageController", function($scope, $location, $routeParams, Venue) {
	$scope.venue = Venue.get($routeParams);
	$scope.back = function() {$location.path('/venues');};
});

musicDbControllers.controller("VenueAdminController", function($scope, $location, $routeParams, Venue) {
	if ($routeParams['venue'] != '0') {
		$scope.venue = Venue.get($routeParams);
	}

	this.save = function() {
		var venue = new Venue({
			canonicalName : this.canonicalName,
			displayName : this.displayName,
			address : this.address,
			description : this.description,
			capacity : this.capacity
		});
		venue.$save();
	}
	
	$scope.cancel = function() {
		$location.path('/venues');
	}
})


