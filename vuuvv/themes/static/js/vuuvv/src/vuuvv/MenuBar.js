define([
    "dojo/_base/declare",
    "dijit/_WidgetBase",
    "dijit/_TemplatedMixin",
    "dojo/text!./templates/MenuBar.html"
], function(declare, _WidgetBase, _TemplateMixin, template) {

return declare("vuuvv.MenuBar",
    [_WidgetBase, _TemplateMixin],
{
    templateString: template
});

});
