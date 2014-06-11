# Copyright 2014 Vypo
#
# message   f=autocomplete_light_registry.py&n=ea8f0b6c7e14e411
# sha256    f0745c597c4f0668a3a7d95dbdafbef08856bc7f614b7d7e53676e47c4b034db
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
import autocomplete_light
from django.contrib.auth.models import User

autocomplete_light.register(User,
    search_fields=['username'],
    attrs={'data-autocomplete-minimum-characters': 3},
    widget_attrs={
        'data-widget-maximum-values': 10,
        'class': 'modern-style'
    }
)
