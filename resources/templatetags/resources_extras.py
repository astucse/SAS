from django import template

register = template.Library()

@register.filter
def plus(arg1,arg2):
    """Removes all values of arg from the given string"""
    return str(arg1)+str(arg2)

@register.simple_tag
def inc(arg1):
    return arg1+1
