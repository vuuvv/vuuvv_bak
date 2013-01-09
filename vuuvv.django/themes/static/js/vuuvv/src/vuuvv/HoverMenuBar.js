define(["dijit/MenuBar"], function(MenuBar) {
	var _ActiveOnMouseoverMixin = dojo.declare(null, {
		onItemHover: function(item) {
			if (!this.isActive) {
				this._markActive();
			}
			this.inherited(arguments);
		}
	});

	return dojo.declare([MenuBar, _ActiveOnMouseoverMixin]);
});
