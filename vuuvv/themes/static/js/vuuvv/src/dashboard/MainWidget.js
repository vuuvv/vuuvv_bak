define([
	"dojo/_base/declare",
	"dijit/_WidgetBase",
	"dijit/_TemplatedMixin",
	"dojo/aspect",
	"dojo/topic",
	"dojo/on",
	"dojo/Stateful",
	"dojo/store/Memory",
	"dojo/store/Observable",
	"./ChildWidget",
	"dojo/text!./templates/MainWidget.html"
], function(
	declare,
	WidgetBase,
	TemplateMixin,
	aspect,
	topic,
	on,
	Stateful,
	Memory,
	Observable,
	ChildWidget,
	template
) {
	return declare([WidgetBase, TemplateMixin], {
		templateString: template,

		timeout: null,
		leaky: false,

		postCreate: function() {
			this.setChildWidget();
			this.setAspect();
			//this.setEvent();
			this.setSubscription();
			this.setStateful();
			this.setObservable();
		},

		setChildWidget: function() {
			var widget = new ChildWidget({ timeout: this.timeout });
			if (!this.leaky) {
				this.own(widget);
			}
		},

		setAspect: function() {
			var someObject = {
					someMethod: function() {}
				},
				signal = aspect.after(someObject, 'someMethod', function() {
					console.warn('aspect.after');
				});

			if (!this.leaky) {
				this.own(signal);
			}

			setTimeout(function() {
				someObject.someMethod();
			}, this.timeout);
		},

		setEvent: function() {
			var handle = on(this.clickableNode, 'click', function(ev) {
				console.warn('on');
			});

			if (!this.leaky) {
				this.own(handle);
			}
		},

		setSubscription: function() {
			var subscription = topic.subscribe('some-topic', function() {
				console.warn('topic.subscribe');
			});

			if (!this.leaky) {
				this.own(subscription);
			}

			setTimeout(function() {
				topic.publish('some-topic', {});
			}, this.timeout);
		},

		setStateful: function() {
			var stateful = new Stateful({a: 'aaa'}),
				handle = stateful.watch('a', function(name, oldVal, newVal) {
					console.warn('Stateful');
				});

			if(!this.leaky) {
				this.own(handle);
			}

			setTimeout(function() {
				stateful.set('a', 'AAA');
			}, this.timeout);
		},

		setObservable: function() {
			var store = Observable(new Memory({
						data: [{ id: 0, a: 'aaa' }]
				})),

				result = store.query(),
				observer = result.observe(function(item, removeIndex, insertedIndex) {
						console.warn('Observale');
				}, true);

			if (!this.leaky) {
				this.own(observer);
			}

			setTimeout(function() {
					store.put({ id: 1, b: 'bbb' });
			}, this.timeout);
		}
	});
});
