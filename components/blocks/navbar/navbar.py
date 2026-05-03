from django_components import Component, register

@register("navbar")
class Navbar(Component):
    template_name = "navbar.html"

    def get_template_data(self, args, kwargs, slots, context):
        
        current_path = kwargs.get("current_path", "/")
        
        items = [
            {"label": "Feed", "href": "/feed/"},
            {"label": "Projects", "href": "/projects/"},
            {"label": "Contact", "href": "/contact/"},
        ]
        
        return {
            "items": items,
            "current_path": current_path
        }
