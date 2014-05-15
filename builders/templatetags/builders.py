from django import template
from django.utils.safestring import mark_safe

register = template.Library()

def stars(value):
    '''Converts a number into raty stars'''
    try:
        value = float(value)
    except ValueError:
        return value
    except TypeError:
        return 0

    return mark_safe('''<div data-raty data-raty-score="{0}"></div>'''.format(value))

register.filter('stars', stars)
