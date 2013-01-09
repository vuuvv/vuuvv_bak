from django.views.generic import TemplateView
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

class View(TemplateView):

    def dispatch(self, request, *args, **kwargs):
        self.authorize()
        return super(View, self).dispatch(request, *args, **kwargs)

    def authorize(self):
        pass

    def get_template_names(self):
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            try:
                return ["%s/%s" % (settings.THEME, self.template_name)]
            except KeyError:
                raise ImproperlyConfigured(
                    "Vuuvv requires a fefinition of THEME in Django settings."
                )
