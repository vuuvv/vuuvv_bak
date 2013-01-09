from flask import Blueprint as _Blueprint

class Blueprint(_Blueprint):

    def route(self, rule, **options):
        def decorator(f):
            endpoint = options.pop("endpoint", f.__name__)
            if hasattr(f, "as_view"):
                f = f.as_view(endpoint)
            self.add_url_rule(rule, endpoint, f, **options)
            return f
        return decorator

