# Copyright 2014 Vypo
#
# message   f=search_indexes.py&n=afa9c4266f5e716b
# sha256    5f4794ed3e90a4f6fd9f2db38591f6d0e43426a8f0fa218ab05c4b3487f740bf
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
from haystack import indexes
from .models import Builder

class BuilderIndex(indexes.SearchIndex, indexes.Indexable):
    title = indexes.CharField(model_attr='name')
    description = indexes.CharField()
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Builder
