var musicDbServices = angular.module('musicDbServices', ['ngResource']);

musicDbServices.factory('Artist', ['$resource',
	function($resource) {
		return $resource('/api/artist/:artist', {}, {
			query: {method:'GET', url:'/api/artist' , isArray:true}
		});
	}
]);