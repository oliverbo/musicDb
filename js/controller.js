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

musicDbControllers.controller("VenueController", function($scope, $location, $modal, Venue, pageInfo) {
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
			
	$scope.export = function() {
		$modal.open({
			templateUrl: 'export.html',
			controller: OkCancelController,
			size: 'sm'
		});
	}
});


musicDbControllers.controller("VenuePageController", function($scope, $location, $routeParams, Venue) {
	$scope.venue = Venue.get($routeParams);
	$scope.back = function() {$location.path('/venues');};
});

musicDbControllers.controller("VenueAdminController", function($scope, $location, $routeParams, $modal, Venue) {
	if ($routeParams['venue'] != '0') {
		$scope.venue = Venue.get($routeParams);
	}

	$scope.saveVenue = function(venue) {	
		var venueResource = new Venue({
			canonicalName : venue.canonicalName,
			displayName : venue.displayName,
			address : venue.address,
			description : venue.description,
			capacity : venue.capacity
		});
		venueResource.$save();
		$scope.venue = new Venue();
	}
	
	$scope.cancel = function() {
		$location.path('/venues');
	}
	
	$scope.delete = function(venue) {
		var modalInstance = $modal.open({
			templateUrl: 'deleteConfirm.html',
			controller: OkCancelController,
			size: 'sm'
		});
	
		modalInstance.result.then(function(ok) {
			var venueResource = new Venue({
				canonicalName : venue.canonicalName
			});
			venueResource.$delete()
			$location.path('/venues');	
		});
	}
})

var OkCancelController = function ($scope, $modalInstance) {
  $scope.ok = function () {
    $modalInstance.close('ok');
  };

  $scope.cancel = function () {
    $modalInstance.dismiss('cancel');
  };
};


