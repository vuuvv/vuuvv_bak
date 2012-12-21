require([
	"dojo/query",
	"dojo/NodeList-dom",
	"dojo/NodeList-data",
	"dojo/NodeList-traverse",
	"dojo/NodeList-manipulate",
	"dojo/domReady!"
], function(query) {

	var is_visible = function(nl) {
		if (nl.length < 1)
			return false;

		var node = nl[0], p

		if (node.domNode) {
			node = node.domNode;
		}

		return (dojo.style(node, "display") != "none") &&
			   (dojo.style(node, "visibility") != "hidden") &&
			   (p = dojo.position(node), p.y + p.h >= 0 && p.x + p.w >= 0 && p.h && p.w);
	}

	var is_hidden = function(nl) {
		return !is_visible();
	}

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
	inputs.on("keyup", function(e) {
		var input = query(this);
		var box = input.parent();

		if (e.keyCode == 13) {
			if (input.filter("#user_name").length > 0) {
				query("#password")[0].focus();
			} else if (input.filter("#password").length > 0) {
				var vcode = $("#vcode");
				if (is_hidden(vcode)) {
					vcode[0].focus();
				} else {
					query("#form_login")[0].submit();
				}
			} else if (input.filter("#vcode")) {
				query("#form_login")[0].submit();
			}
		}
	});
	inputs.on("keydown", function(e) {
		if (e.keyCode == 13) {
			e.preventDefault();
		}
	});
	inputs[0].focus();
});
