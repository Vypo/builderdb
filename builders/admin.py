# Copyright 2014 Vypo
#
# message   f=admin.py&n=bff9e84257389e6f
# sha256    8d3f1cbb7c4f62cc6a1b008b7a93984eebe9929d75239c9627952daec0e7b352
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
from django.contrib import admin
from .models import Builder, Website, Review, Photo

class BuilderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Builder, BuilderAdmin)

class WebpageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Website, WebpageAdmin)

class ReviewAdmin(admin.ModelAdmin):
    pass

admin.site.register(Review, ReviewAdmin)

class PhotoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Photo, PhotoAdmin)
