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

@manager.option('-m', '--mode', dest='mode', default='dev')
def startserver(mode):
    config_app(modes[mode])
    server = Server(
        use_debugger = True,
        use_reloader = True,
        host = '0.0.0.0')

if __name__ == '__main__':
    import pdb;pdb.set_trace()
    manager.run()
