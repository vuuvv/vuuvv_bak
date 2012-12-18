var profile = (function(){
    return {
        basePath: "./src",
        releaseDir: "../../app",
        releaseName: "lib",
        action: "release",
 
        packages:[{
            name: "dojo",
            location: "dojo"
        },{
            name: "dijit",
            location: "dijit"
        },{
            name: "dojox",
            location: "dojox"
        },{
            name: "app",
            location: "app"
        }],
 
        layers: {
            "dojo/dojo": {
                include: [ "dojo/dojo", "dojo/i18n", "dojo/domReady",
                    "app/main", "app/run" ],
                customBase: true,
                boot: true
            },
            "app/Dialog": {
                include: [ "app/Dialog" ]
            }
        }
    };
})();

