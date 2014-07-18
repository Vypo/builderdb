# Copyright 2014 Vypo
#
# message   f=sitetrees.py&n=360b3709cf89148e
# sha256    6aad5ab3be9869d38ca50be9df129d1563f062bc4d70a72d59f17ffe8f3af283
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
from sitetree.utils import tree, item

sitetrees = (
    tree('builders', items=[
        item('Builders', 'builder.list', children=[
            item('Search', 'builder.search', in_menu=False, in_sitetree=False),
            item('{{ builder.name }}', 'builder.detail builder.slug', in_menu=False, in_sitetree=False, children=[
                item('Reviews', 'review.list builder.slug', in_menu=False, in_sitetree=False, children=[
                    item('{{ review.costume_name }} by {{ builder.name }}', 'review.detail builder.slug review.slug', in_menu=False, in_sitetree=False, children=[
                        item('Photo #{{ photo.pk }}', 'photo.detail builder.slug review.slug photo.pk', in_menu=False, in_sitetree=False, children=[
                            item('Delete', 'photo.delete builder.slug review.slug photo.pk', in_menu=False, in_sitetree=False),
                        ]),

                        item('Edit', 'review.edit builder.slug review.slug', in_menu=False, in_sitetree=False, children=[
                            item('New Photo', 'photo.create builder.slug review.slug', in_menu=False, in_sitetree=False),
                        ]),

                        item('Delete', 'review.delete builder.slug review.slug', in_menu=False, in_sitetree=False),

                    ]),
                ]),
                item('Edit', 'builder.edit builder.slug', in_menu=False, in_sitetree=False),
                item('Delete', 'builder.delete builder.slug', in_menu=False, in_sitetree=False),

                item('New Review', 'review.create builder.slug', in_menu=False, in_sitetree=False),
            ]),

        ])
    ]),
)
