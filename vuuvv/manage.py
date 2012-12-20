import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server
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
