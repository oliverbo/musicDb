var musicDbControllers = angular.module('musicDbControllers', ['musicDbServices', 'pageModule']);

musicDbControllers.controller("PageHeaderController", function($scope, pageInfo) {
	$scope.userName = pageInfo.userName;
	$scope.logoutURI = pageInfo.logoutURI;
	$scope.loginURI = pageInfo.loginURI;
	pageInfo.isAdmin ? $scope.isAdmin = true : $scopeIsAdmin = false;
	
	$scope.alerts = [];
});

musicDbControllers.controller("VenueController", function($scope, $location, $modal, Venue, pageInfo) {
	$scope.venues = Venue.query();
	pageInfo.isAdmin ? $scope.isAdmin = true : $scope.isAdmin = false;
	$scope.showVenue = function(venue) {
		if (pageInfo.isAdmin) {
			$location.path('/admin/venues/' + venue.uniqueName);	
		} else {
			$location.path('/venues/' + venue.uniqueName);
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
	
	$scope.import = function() {
		var modalInstance = $modal.open({
			templateUrl: 'import.html',
			controller: ImportController,
			size: 'sm'
		})
		
		modalInstance.result.then(function(file) {
			console.log('Upload ' + file);
		})
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
		var venueResource = new Venue(venue);
		venueResource.$save(function(success) {
			$scope.alerts.length = 0;
			$scope.alerts[0] = { type : "success", message : "Venue saved"};
			$scope.venue = new Venue();	
		}, function(error) {
			$scope.alerts.length = 0;
			$scope.alerts[0] = { type : "danger", message : error.data.errorMessage };
			if (error.data.details) {
				for (i = 0; i < error.data.details.length; i++) {
					errorDetails = error.data.details[i];
					$scope.alerts[i+1] = { type : "danger", message : errorDetails.field + ": " + errorDetails.errorMessage };
				}
			}
		});
	}
	
	$scope.cancel = function() {
		$scope.alerts.length = 0;
		$location.path('/venues');
	}
	
	$scope.delete = function(venue) {
		$scope.alerts.length = 0;
		var modalInstance = $modal.open({
			templateUrl: 'deleteConfirm.html',
			controller: OkCancelController,
			size: 'sm'
		});
	
		modalInstance.result.then(function(ok) {
			var venueResource = new Venue({
				uniqueName : venue.uniqueName
			});
			venueResource.$delete()
			$location.path('/venues');	
		});
	}
})

var ImportController = function ($scope, $modalInstance) {
  $scope.upload = function (file) {
  	console.log("----> " + file);
    $modalInstance.close(file);
  };

  $scope.cancel = function () {
    $modalInstance.dismiss('cancel');
  };
};

var OkCancelController = function ($scope, $modalInstance) {
  $scope.ok = function () {
    $modalInstance.close('ok');
  };

  $scope.cancel = function () {
    $modalInstance.dismiss('cancel');
  };
};


