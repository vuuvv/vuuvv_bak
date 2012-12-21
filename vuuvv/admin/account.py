from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView

from flask.ext.mongoengine.wtf import model_form

from vuuvv.account.models import User, Role, Permission

account = Blueprint('account', __name__, template_folder='templates')

class UserList(MethodView):
    cls = User

    def get(self):
        users = self.cls.objects.all()
        return render_template('admin/list.html', posts=posts)

class RoleDetail(MethodView):

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
        return render_template('admin/detail.html', **context)

    def post(self, id):
        context = self.get_context(id)
        form = context.get('form')

        if form.validate():
            role = context.get('role')
            form.populate_obj(role)
            role.save()

            return redirect(url_for('admin.create'))
        return render_template('admin/detail.html', **context)

account.add_url_rule('/role/<id>/', view_func=RoleDetail.as_view('edit'))
account.add_url_rule('/role/create/', defaults={'id': None}, view_func=RoleDetail.as_view('create'))
