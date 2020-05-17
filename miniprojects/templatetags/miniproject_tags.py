from django import template
from ..models import Miniproject
# Markdown is a text-to-HTML conversion tool
from django.utils.safestring import mark_safe
import markdown



register = template.Library()

@register.simple_tag
def total_miniproject():
    return Miniproject.objects.count()

@register.inclusion_tag('miniprojects/miniproject/most_important_miniproject.html')
def most_important_miniproject(num=5):
    choices = Miniproject.objects.all()[:num]
    return {'choices': choices}

@register.filter
def cut(value, arg):
    return value.replace(arg, ' ')

# register markdown filter
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


