# Copyright 2014 Vypo
#
# message   f=builders.py&n=acf190c1cf2abb31
# sha256    23e448c2f31a41fecbd7d63fb90ace31c0cdca90aeb2c0a876f6393ed8600cff
#
# This file is part of BuilderDB.
#
# BuilderDB is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BuilderDB is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with BuilderDB.  If not, see <http://www.gnu.org/licenses/>.
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

def stars(value, name=None):
    '''Converts a number into raty stars'''
    try:
        value = float(value)
    except ValueError:
        return value
    except TypeError:
        return 0

    if name is None:
        return mark_safe('''<div data-raty data-raty-score="{0}"><meta itemprop="ratingValue" content="{0}"></div>'''.format(value))
    else:
        return mark_safe('''<div data-raty data-raty-score="{0}" data-raty-editable></div>'''.format(value))

register.filter('stars', stars)
