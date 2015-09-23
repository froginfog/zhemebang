# -*- coding: utf-8 -*-

from django import template
register = template.Library()


def do_list(v):
    return range(0, v)


register.filter('do_list', do_list)