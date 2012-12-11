from django.views.generic import TemplateView

class AuthView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        self.authorize()
        super(AuthView, self).dispatch(request, *args, **kwargs)

    def authorize(self):
        pass
