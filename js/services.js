var musicDbServices = angular.module('musicDbServices', ['ngResource']);

musicDbServices.factory('Artist', ['$resource',
	function($resource) {
		return $resource('/api/artist/:artist', {}, {
			query: {method:'GET', url:'/api/artist' , isArray:true},
			save: {method:'POST'}
		});
	}
]);

musicDbServices.factory('Venue', ['$resource',
	function($resource) {
		return $resource('/api/venue/:venue', {venue : "@id"}, {
			query: {method:'GET', url:'/api/venue' , isArray:true}
		});
	}
]);
