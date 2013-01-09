from flask import request, render_template
from flask.views import MethodView

class Login(MethodView):
    rules = (
        {"rule": "/login", "endpoint": "login"},
    )

    def get(self):
        return render_template('dashboard/login.html')
