from django import template

register = template.Library()

@register.filter
def plus(arg1,arg2):
    """Removes all values of arg from the given string"""
    return str(arg1)+str(arg2)
