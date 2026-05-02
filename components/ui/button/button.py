from django_components import Component, register

@register("button")
class Button(Component):
    template_file = "button.html"

    def get_context_data(self, variant="default", size="default", as_child=False, class_name="", **kwargs):
        base_classes = (
            "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md "
            "text-sm font-medium transition-all disabled:pointer-events-none disabled:opacity-50 "
            "[&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 shrink-0 "
            "[&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 "
            "focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 "
            "aria-invalid:border-destructive"
        )

        variants = {
            "default": "bg-white text-primary-foreground hover:bg-primary/90",
            "destructive": "bg-destructive text-white hover:bg-destructive/90 focus-visible:ring-destructive/20 dark:focus-visible:ring-destructive/40 dark:bg-destructive/60",
            "shadow": "bg-white border border-neutral-400 shadow-xs hover:bg-neutral-100 hover:text-accent-foreground dark:bg-input/30 dark:border-input dark:hover:bg-input/50",
            "secondary": "bg-secondary text-secondary-foreground hover:bg-secondary/80",
            "ghost": "hover:bg-accent hover:text-accent-foreground dark:hover:bg-accent/50",
            "link": "text-primary underline-offset-4 hover:underline",
            "text": "px-3 py-1.5 text-sm font-medium bg-transparent hover:bg-accent/50 rounded-md outline-none focus:bg-accent/50 transition-colors",
        }

        sizes = {
            "default": "h-9 px-4 py-2 has-[>svg]:px-3",
            "sm": "h-8 rounded-md gap-1.5 px-3 has-[>svg]:px-2.5",
            "lg": "h-10 rounded-md px-6 has-[>svg]:px-4",
            "icon": "size-9",
            "icon-sm": "size-8",
            "icon-lg": "size-10",
        }

        variant_classes = variants.get(variant, variants["default"])
        size_classes = sizes.get(size, sizes["default"])

        final_classes = f"{base_classes} {variant_classes} {size_classes} {class_name}".strip()

        return {
            "final_classes": final_classes,
            "as_child": as_child,
            "extra_props": kwargs
        }
