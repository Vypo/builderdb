from sitetree.utils import tree, item

sitetrees = (
    tree('builders', items=[
        item('Builders', 'builder.list', children=[
            item('{{ builder.name }}', 'builder.detail builder.slug', in_menu=False, in_sitetree=False, children=[
                item('Reviews', 'review.list builder.slug', in_menu=False, in_sitetree=False, children=[
                    item('{{ review.costume_name }} by {{ builder.name }} Review', 'review.detail builder.slug review.slug', in_menu=False, in_sitetree=False),
                ]),
            ]),

            item('Edit "{{ builder.name }}"', 'builder.edit builder.slug', in_menu=False, in_sitetree=False),
            item('Delete "{{ builder.name }}"', 'builder.delete builder.slug', in_menu=False, in_sitetree=False),
        ])
    ]),
)
