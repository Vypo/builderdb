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
