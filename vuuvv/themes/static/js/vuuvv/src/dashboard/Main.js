define([
	'vuuvv/Application'
], function(
	Application
) {
	return dojo.declare([Application], {
		routes: [
			['/user/', 'user']
		],

		user: function(evt) {
			alert('user');
		}
	});
});
