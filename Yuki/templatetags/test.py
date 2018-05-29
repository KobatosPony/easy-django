# coding:utf-8
from django import template

register = template.Library()


# 注册自定义标签
@register.simple_tag()
def test(string_arg):
    return str(string_arg)


# 注册自定义过滤器
@register.filter()
def test_filter(value, arg):
    return str(value).replace(arg, "worked!")



