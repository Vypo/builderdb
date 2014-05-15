from django import forms
from django.forms.models import modelform_factory, modelformset_factory, inlineformset_factory
from django.core.validators import ValidationError, URLValidator
from .models import Builder, Website
from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import (Layout, Submit, Fieldset, Row,
                                            Column, ButtonHolder, HTML)
import autocomplete_light

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

    def __init__(self, *args, **kwargs):
        super(DeleteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Are you sure you want to delete "' + unicode(self.instance) + '"?',
                Row(
                    Column(ButtonHolder(
                        Submit('submit', 'Delete', css_class='alert'),
                        HTML('<a class="button" href="' + self.instance.get_absolute_url() + '">Go Back</a>')
                    ), css_class='small-12')
                )
            )
        )
