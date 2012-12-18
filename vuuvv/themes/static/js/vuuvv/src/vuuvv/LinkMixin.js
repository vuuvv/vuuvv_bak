define([], function() {
	return dojo.declare(null, {
		href: null,
		onClick: function() {
			window.location.href = this.href;
			this.inherited(arguments);
		}
	});
});
