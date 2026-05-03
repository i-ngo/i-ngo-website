from django_components import Component, register
@register("contact")
class Contact(Component):
    template_file = "contact.html"
    js_file = "contact.js"
    css_file = "contact.css"

    class Kwargs:
        param: str = "sample value"

    def get_template_data(self, args, kwargs: Kwargs, slots, context):
        return {
            "param": kwargs.param,
        }
