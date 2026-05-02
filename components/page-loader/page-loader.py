from django_components import Component, register

# TODO: Decide on dark mode theme, then come back and do ts
@register("page-loader")
class Pageloader(Component):
    template_file = "page-loader.html"
    js_file = "page-loader.js"
    css_file = "page-loader.css"

    class Kwargs:
        param: str = "sample value"

    def get_template_data(self, args, kwargs: Kwargs, slots, context):
        return {
            "param": kwargs.param,
        }
