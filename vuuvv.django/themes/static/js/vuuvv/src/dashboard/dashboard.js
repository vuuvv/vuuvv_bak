require([
		"dojo/dom", "dojo/_base/fx", "dojo/domReady!"
], function(dom, fx) {
	setTimeout(function() {
		setTimeout(function() {
			fx.fadeOut({
				node: 'loading_overlay',
				duration: 500,
				onEnd: function(n) {
					n.style.display = "none";
				}
			}).play();
		}, 250);
	}, 320);
});
