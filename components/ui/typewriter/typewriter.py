from django_components import Component, register

@register("typewriter")
class TypewriterComponent(Component):
    template_name = "typewriter.html"
    css_file = "typewriter.css"

    def get_context_data(self, phrases=None, **kwargs):
        if not phrases:
            phrases = [
            "Python, Django, FastApi.",
            "Linux, Bash, Docker.",
            "Automation, Design, VAPT.",
        ]
            
        return {
            "phrases": phrases
        }
