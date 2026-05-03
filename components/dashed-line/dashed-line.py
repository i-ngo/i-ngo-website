from django_components import Component, register

@register("dashed-line")
class DashedLine(Component):
    template_file = "dashed-line.html"

    class Kwargs:
        orientation: str = "horizontal"
        class_name: str = ""

    def get_template_data(self, args, kwargs: Kwargs, slots, context):
        is_horizontal = kwargs.orientation == "horizontal"
        
        return {
            "is_horizontal": is_horizontal,
            "class_name": kwargs.class_name,
        }
