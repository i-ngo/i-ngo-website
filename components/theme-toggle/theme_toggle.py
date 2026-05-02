from django_components import Component, register

@register("theme-toggle")
class Theme_toggle(Component):
    template_file = "theme-toggle.html"
    js_file = "theme-toggle.js"
