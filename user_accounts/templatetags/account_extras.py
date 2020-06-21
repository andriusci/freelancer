from django import template
register = template.Library()

@register.filter
def index(indexable, i):
    return indexable[i:]

@register.simple_tag
def condition(value="False"):
  return value