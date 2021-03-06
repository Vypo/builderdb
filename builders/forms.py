# Copyright 2014 Vypo
#
# message   f=forms.py&n=4fdaaa28e47d5f11
# sha256    e4a61499d3352361f9239e94683f3a7caaa057cbcdca1ecaa10c2c21ac2e6a0f
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
from django import forms
from django.contrib.contenttypes.forms import generic_inlineformset_factory
from django.forms.models import modelform_factory, modelformset_factory, inlineformset_factory
from django.forms.widgets import Widget
from django.core.validators import ValidationError, URLValidator
from .models import Builder, Website, Review, Photo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import LayoutObject
from crispy_forms.utils import render_field
from crispy_forms_foundation.layout import (Layout, Submit, Fieldset, Row,
                                            Column, ButtonHolder, HTML, Div)
import autocomplete_light

class RatyWidget(Widget):
    def render(self, name, value, attrs=None):
        try:
            value = float(value)
        except:
            value = 0
        return '''
<div data-raty data-raty-rw data-raty-score="{0}" data-raty-name="{2}"></div>
'''.format(value, attrs['id'], name)

class BuilderForm(autocomplete_light.ModelForm):
    class Meta:
        model = Builder
        exclude = []

    other_sites = forms.CharField(required=False, widget=forms.Textarea(),
                                    help_text='one address per line')

    def __init__(self, *args, **kwargs):
        super(BuilderForm, self).__init__(*args, **kwargs)
        self.fields['other_sites'].initial = '\n'.join(x.url for x in self.instance.other_sites.all())
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('The Basics',
                        Row(
                            Column('name', css_class='small-12 medium-6'),
                            Column('status', css_class='small-12 medium-6')
                        ),

                        Row(
                            Column('description', css_class='small-12')
                        )
            ),

            Fieldset('More Information',
                        'other_sites'),

            Fieldset('Look & Feel',
                        Row(
                            Column('thumb', css_class='small-12 medium-6'),
                            Column('banner', css_class='small-12 medium-6'),
                        )
            ),

            Fieldset('Administration',
                'users'),

            ButtonHolder(
                Submit('submit', 'Save'),
                HTML('<a class="button secondary" href="'
                        + self.instance.get_absolute_url() + '">Cancel</a>')
            )
        )

    def clean_other_sites(self):
        urls = self.cleaned_data['other_sites'].split('\r\n')
        validator = URLValidator()
        for url in urls:
            if len(url) > 0:
                validator(url)
        return urls

    def save(self, *args, **kwargs):
        urls = self.cleaned_data['other_sites']
        # TODO: only delete/add the minimum required

        # Delete URLS
        self.instance.other_sites.all().delete()

        # Add new urls
        Website.objects.bulk_create([Website(builder=self.instance, url=x) for x in urls if len(x.strip())])

        return super(BuilderForm, self).save(*args, **kwargs)

class DeleteForm(forms.ModelForm):
    class Meta:
        fields = []

    @classmethod
    def create_for(cls, obj):
        return modelform_factory(type(obj), form=cls)(instance=obj)

    def get_cancel_url(self):
        return self.instance.get_absolute_url()

    def __init__(self, *args, **kwargs):
        super(DeleteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Are you sure you want to delete "{0}"?'.format(self.instance),
                Row(
                    Column(ButtonHolder(
                        Submit('submit', 'Delete', css_class='alert'),
                        HTML('<a class="button secondary" href="'
                                + self.get_cancel_url() + '">Go Back</a>')
                    ), css_class='small-12')
                )
            )
        )

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['user', 'builder']
        widgets = {
            'construction': RatyWidget,
            'communication': RatyWidget,
            'timeliness': RatyWidget,
            'commission_date': forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}),
            'received_date': forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}),
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        if 'builder' in kwargs['initial']:
            builder = kwargs['initial']['builder']
            self.instance.builder = builder
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('Basic Information',
                Row(
                    Column('costume_name', css_class='small-12')
                ),
                Row(
                    Column('commission_date', css_class='small-12 medium-6'),
                    Column('received_date', css_class='small-12 medium-6')
                ),
            ),

            Fieldset('Details',
                Row(
                    Column('text', css_class='small-12')
                )
            ),

            Fieldset('Rating',
                Div('construction',
                    'communication',
                    'timeliness')
            ),

            ButtonHolder(
                Submit('submit', 'Save'),
                HTML('<a class="button secondary" href="'
                        + (self.instance.get_absolute_url() if self.instance.pk is not None else builder.get_absolute_url()) + '">Cancel</a>')
            )
        )

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['content_object', 'object_id', 'content_type']

    def __init__(self, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        if 'content_object' in kwargs['initial']:
            context_object = kwargs['initial']['content_object']
            self.instance.content_object = context_object
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('Photo',
                Row(
                    Column('image', css_class='small-12'),
                ),
                Row(
                    Column('caption', css_class='small-12 medium-9'),
                    Column('priority', css_class='small-12 medium-3'),
                )
            ),
            ButtonHolder(
                Submit('submit', 'Save'),
                HTML('<a class="button secondary" href="'
                        + self.instance.content_object.get_absolute_url() + '">Cancel</a>')
            )
        )
