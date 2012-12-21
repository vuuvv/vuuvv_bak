define([
	"./MainWidget",
	"dojo/domReady!"
], function (MainWidget) {
	var timeout = 3000,
		widget = new MainWidget({
			timeout: timeout,
			leaky: false
		}, 'widget');
	
	widget.startup();

	setTimeout(function() {
		widget.destroy(true);
		console.info('Widget is now destroyed while preserving the dom');
	}, timeout - 1000);
});
