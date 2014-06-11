# Copyright 2014 Vypo
#
# message   f=views.py&n=aeacc85be87ec4c6
# sha256    716e958cbb152704dfa68792ae2ad8046fe2b421a9eaaf104025077aac6f7e5d
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
from django.shortcuts import render
from django.views.generic import TemplateView

class SettingsView(TemplateView):
    template_name = 'accounts/settings.html'
