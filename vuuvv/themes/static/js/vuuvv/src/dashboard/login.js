require([
	"dojo/query",
	"dojo/NodeList-dom",
	"dojo/NodeList-data",
	"dojo/NodeList-traverse",
	"dojo/NodeList-manipulate",
	"dojo/domReady!"
], function(query) {
	var inputs = query(".textbox input").data("empty", true);
	inputs.on("focus", function(e) {
		var input = query(this);
		var box = input.parent();
		box.addClass("textbox-focus")
			.removeClass("textbox-error")
			.removeClass("textbox-tip");
		query("#btn_login").parent().removeClass("buttons-errors");

		if (input.val() == input.attr('tip'))
			input.val('');
	});
	inputs.on("blur", function(e) {
		var input = query(this);
		var box = input.parent();
		box.removeClass("textbox-focus");

		if (!input.val() || input.val() == input.attr('tip')) {
			input.val(input.attr("tip"));
			box.addClass("textbox-tip");
		}
	});
	inputs[0].focus();
});
