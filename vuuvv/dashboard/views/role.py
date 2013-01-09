from flask import request, redirect, render_template, url_for
from flask.views import MethodView
from flask.ext.mongoengine.wtf import model_form
from vuuvv.account.models import Role

class RoleDetail(MethodView):
    rules = (
        {"rule": "/role/<id>/", "endpoint": "edit"},
        {"rule": "/role/create/", "endpoint": "create",
         "defaults": {"id": None}},
    )

    def get_context(self, id=None):
        form_cls = model_form(Role, exclude=('created_at',))

        if id:
            role = Role.objects.get_or_404(pk=id)
            if request.method == 'POST':
                form = form_cls(request.form, inital=role._data)
            else:
                form = form_cls(obj=role)
        else:
            role = Role()
            form = form_cls(request.form)

        return {
            'role': role,
            'form': form,
            'create': id is None
        }

    def get(self, id):
        context = self.get_context(id)
        return render_template('dashboard/detail.html', **context)

    def post(self, id):
        context = self.get_context(id)
        form = context.get('form')

        if form.validate():
            role = context.get('role')
            form.populate_obj(role)
            role.save()

            return redirect(url_for('dashboard.create'))
        return render_template('dashboard/detail.html', **context)
