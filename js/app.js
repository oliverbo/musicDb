var musicDbApp = angular.module('musicDbApp', 
	['pageModule', 'musicDbServices', 'ngRoute', 'musicDbControllers', 'ui.bootstrap']);
	
musicDbApp.config(['$routeProvider',
	function($routeProvider) {
		$routeProvider.
			when('/artists', {
				templateUrl : 'html/partials/artists.html',
				controller : 'ArtistController'
			}).
			when('/venues', {
				templateUrl : 'html/partials/venues.html',
				controller : 'VenueController'
			}).
			otherwise({
				redirectTo : '/venues'
			});		
		}
	]);