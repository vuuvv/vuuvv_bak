define([
		'vuuvv/Application',
		'vuuvv/HoverMenuBar',
		'dijit/Menu',
		'dijit/MenuItem',
		'dijit/layout/BorderContainer',
		'dijit/layout/TabContainer',
		'dijit/PopupMenuItem',
		'dijit/PopupMenuBarItem'
], function(
	Application,
	HoverMenuBar,
	Menu,
	MenuItem,
	BorderContainer,
	TabContainer,
	PopupMenuItem,
	PopupMenuBarItem
) {
	return dojo.declare([Application], {
		routes: [
			['/user/', 'user']
		],

		id: 'main',

		menus: [
			{
				label: 'System',
				children: [
					{ label: 'Settings' },
					{ label: 'FileManage' },
					{ label: 'Logout' }
				]
			},
			{
				label: 'Account',
				children: [
					{ label: 'User' },
					{ label: 'Role' },
					{ label: 'Permission'}
				]
			}
		],

		constructor: function() {
			var layout = new BorderContainer({
				design: 'headline',
				liveSplitters: false
			}, this.id);

			var menu_bar = this.create_menu();
			layout.addChild(menu_bar);

			var tabs = new TabContainer({
				region: "center",
				id: "content_tabs",
			});

			layout.addChild(tabs);

			layout.startup();
		},

		create_menu_item: function(info) {
			if (info.children) {
				var menu = new Menu({});
				var children = info.children;
				for (var i = 0; i < children.length; i++) {
					menu.addChild(this.create_menu_item(children[i]));
				}
				return new PopupMenuItem({
					label: info.label,
					popup: menu
				});
			} else {
				return new MenuItem( {label: info.label} );
			}
		},

		create_menu: function() {
			var menubar = new HoverMenuBar({
				region: 'top',
				popupDelay: 100
			});

			var menus = this.menus;

			for (var i = 0; i < menus.length ; i++) {
				var menu_info = menus[i];
				var menu = new Menu({
				});

				for (var j = 0; j < menu_info.children.length; j++) {
					menu.addChild(this.create_menu_item(menu_info.children[j]));
				}
				
				var popup_item = new PopupMenuBarItem({
					label: menu_info.label,
					popup: menu
				});

				menubar.addChild(popup_item);
			}
			return menubar;
		},

		user: function(evt) {
		}
	});
});
