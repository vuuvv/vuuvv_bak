define([
	"dojo/_base/declare",
	"dijit/_WidgetBase"
], function (
	declare,
	WidgetBase
) {
	return declare([WidgetBase], {
			
			timeoutId: null,

			timeout: null,

			postCreate: function() {
				this.timeoutId = setTimeout(function() {
						console.warn('child widget');
				}, this.timeout);
			},

			destroy: function() {
				this.inherited(arguments);
				clearTimeout(this.timeoutId);
			}
	});
});
