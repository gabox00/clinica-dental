from django import template

register = template.Library()

@register.filter(name='colorStatus')
def colorStatus(status):
    if status == 1:
        return "#5cb85c"
    elif status == 0:
        return "red"
    else: 
        return "#3788d8"