from sitetree.utils import tree, item

sitetrees = (
    tree('builders', items=[
        item('Builders', 'builder.list', children=[
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
