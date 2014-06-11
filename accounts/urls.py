# Copyright 2014 Vypo
#
# message   f=urls.py&n=67dc6da2e9d262cf
# sha256    1fd0224958e53d80e8ae61398c3b5dfb110c90a315e1c1627f68fe6fd20fe26f
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
from django.conf.urls import include, url
from .views import SettingsView

urlpatterns = [
    # Examples:
    # url(r'^$', 'builderdb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', SettingsView.as_view(), name='accounts_index'),

]
