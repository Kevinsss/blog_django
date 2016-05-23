# coding:utf-8
import markdown

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


# 以上语句
@register.filter(name="my_markdown")
def my_markdown(value):
	return mark_safe(markdown.markdown(value))
