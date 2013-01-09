import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../libs/')))

from flask.ext.script import Manager, Server, Command, Option
from vuuvv import app, db
from vuuvv.config import Development, Production, Testing

manager = Manager(app)

modes = {
    'dev': Development,
    'product': Production,
    'test': Testing
}

def config_app(config=None):
    if config:
        app.config.from_object(config)
    db.init_app(app)

manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)

class ShowUrls(Command):
    """
    Displays all of the url matching routes for the project.
    """
    def __init__(self, order='rule'):
        self.order = order

    def get_options(self):
        options = super(ShowUrls, self).get_options()
        options += Option('--order',
                          dest='order',
                          default=self.order,
                          help='Property on Rule to order by (default: %s)' % self.order,
                          ),

        return options

    def run(self, order):
        from flask import current_app

        print "%-30s" % 'Rule', 'Endpoint'
        print '-' * 80

        rules = sorted(current_app.url_map.iter_rules(), key=lambda rule: getattr(rule, order))
        for rule in rules:
            print "%-30s" % rule, rule.endpoint

manager.add_command("show_urls", ShowUrls())

def register_blueprints(app):
    from vuuvv.admin.account import account
    app.register_blueprint(account)

@manager.option('-t', '--host', dest='host', default='0.0.0.0')
@manager.option('-p', '--port', dest='port', type=int, default=5000)
@manager.option('--threaded', dest='threaded', action='store_true', default=False)
@manager.option('--processes', dest='processes', type=int, default=1)
@manager.option('--passthrough-errors', dest='passthrough_errors', action='store_true', default=False)
@manager.option('-m', '--mode', dest='mode', default='dev')
def startserver(mode, host, port, threaded, processes, passthrough_errors):
    config_app(modes[mode])
    use_debugger = False
    use_reloader = False
    if mode == 'dev':
        use_debugger = True
        use_reloader = True

    register_blueprints(app)
    import pdb;pdb.set_trace()

    app.run(host=host,
            port=port,
            debug=app.config.get('DEBUG', use_debugger),
            use_debugger=use_debugger,
            use_reloader=use_reloader,
            threaded=threaded,
            processes=processes,
            passthrough_errors=passthrough_errors)

if __name__ == '__main__':
    manager.run()
