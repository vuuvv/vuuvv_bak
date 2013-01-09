define([
	'dojo/_base/lang',
	'dojo/router',
	'dojo/Stateful'
], function(
	lang,
	router,
	Stateful
) {
	return dojo.declare([Stateful], {
		routes: [],

		constructor: function() {
			var routes = this.routes;
			for (var i = 0, len=routes.length; i < len; i++) {
				var route = routes[i];
				router.register(route[0], lang.hitch(this, route[1]));
			}
			router.startup();
		}
	});
});
