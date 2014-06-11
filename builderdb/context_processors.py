# Copyright 2014 Vypo
#
# message   f=context_processors.py&n=c5afad38fee015ce
# sha256    1291b1447080dfdd0c61f7413859851bda3acd8d5b21906306bd457498933ad8
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
from django.contrib.sites.models import Site

def site(request):
    return {
        'site': Site.objects.get_current()
    }
