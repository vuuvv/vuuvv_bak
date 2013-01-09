require({
    baseUrl: '/static/js/vuuvv/src',
    packages: [
        'dojo',
        'dijit',
        'dojox',
        'vuuvv'
    ]
}, ["dojo/parser", 'vuuvv/MenuBar', "dojo/domReady!"], function(parser) {
    parser.parse();
});
