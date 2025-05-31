from django import template

register = template.Library()

@register.inclusion_tag("user_app/inclusion_tags/custom_form.html")
def render_custom_form(form):
    '''
    
    '''
    return {"form": form}