var musicDbApp = angular.module('musicDbApp', 
	['pageModule', 'musicDbServices', 'ngRoute', 'musicDbControllers', 'ui.bootstrap']);
	
musicDbApp.config(['$routeProvider',
	function($routeProvider) {
		$routeProvider.
			when('/artists', {
				templateUrl : '/partials/artists.html',
				controller : 'ArtistController'
			}).
			when('/venues', {
				templateUrl : '/partials/venues.html',
				controller : 'VenueController'
			}).
			when('/admin/venues/:venueId', {
				templateUrl : '/partials/venuePageAdmin.html',
				controller : 'VenueAdminController'
			}).
			when('/venues/:venueId', {
				templateUrl : '/partials/venuePage.html',
				controller : 'VenuePageController'
			}).
			otherwise({
				redirectTo : '/venues'
			});
	}
]);