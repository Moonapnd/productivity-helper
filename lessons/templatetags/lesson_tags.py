from django import template
from ..models import Lesson
# Markdown is a text-to-HTML conversion tool
from django.utils.safestring import mark_safe
import markdown


register = template.Library()

@register.simple_tag
def total_lesson():
    return Lesson.objects.count()

@register.inclusion_tag('lessons/lesson/most_important_lesson.html')
def most_important_lesson(num=5):
    choices = Lesson.objects.all()[:num]
    return {'choices': choices}

@register.filter
def cut(value, arg):
    return value.replace(arg, ' ')

# register markdown filter
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))



