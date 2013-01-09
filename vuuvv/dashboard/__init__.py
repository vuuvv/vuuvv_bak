import os
import sys
import inspect

from flask import Blueprint
from flask import current_app as app
from flask.views import MethodView

class Dashboard(object):

    def __init__(self):
        bps = [self._import_blueprint(b) for b in self._find_blueprints()]
        for bp in bps:
            self._register_blueprint(bp)

    def _find_blueprints(self):
        directory = self._get_views_path()
        bps = []
        for file in os.listdir(directory):
            name, ext = os.path.splitext(file)
            if ext == ".py" and name != "__init__":
                bps.append("views.%s" % name)
        return bps

    def _get_views_path(self):
        path = sys.modules[self.__class__.__module__].__file__
        return os.path.join(os.path.dirname(path), "views")

    def _import_blueprint(self, name):
        prefix = self.__class__.__module__
        import_name = "%s.%s" % (prefix, name)
        __import__(import_name)
        return sys.modules[import_name]

    def _register_blueprint(self, module):
        name = module.__name__
        blueprint = Blueprint(name.split(".")[-1], name,
                              url_prefix="/dashboard", template_folder="templates")
        views = []
        for attr in dir(module):
            view = getattr(module, attr)
            if view != MethodView and inspect.isclass(view) and issubclass(view, MethodView):
                for rule in view.rules:
                    rule["view_func"] = view.as_view(rule["endpoint"])
                    blueprint.add_url_rule(**rule)

        app.register_blueprint(blueprint)

    def render(self):
        pass

    def get_menus(self):
        pass

