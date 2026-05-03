from django_components import Component, register

# TODO: Make the background more stylish. Thinking maybe the gradient middle can have a mountain range
#		drawn in to create a sky and water effect.

@register("background")
class Background(Component):
    template_file = "background.html"

    class Kwargs:
        variant: str = "top"
        class_name: str = ""

    def get_template_data(self, args, kwargs: Kwargs, slots, context):
        base_classes = "relative mx-2.5 mt-2.5 lg:mx-4 bg-gradient-to-b"
        
        if kwargs.variant == "top":
            variant_classes = (
                "from-bg via-white to-bg/80 via-20% rounded-t-4xl rounded-b-2xl "
                "dark:from-blueiris dark:via-darkbg dark:to-blueiris/80"
            )
        elif kwargs.variant == "bottom":
            variant_classes = (
                "from-bg via-white to-bg rounded-t-2xl rounded-b-4xl "
                "dark:from-darkbg dark:via-blueiris dark:to-darkbg"
            )
        else:
            variant_classes = ""

        final_classes = f"{base_classes} {variant_classes} {kwargs.class_name}".strip()

        return {
            "final_classes": final_classes,
        }
