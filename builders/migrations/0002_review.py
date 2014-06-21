# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
from django.conf import settings
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('builders', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('builder', models.ForeignKey(to='builders.Builder', to_field='id')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('costume_name', models.CharField(max_length=1024)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
                ('text', markupfield.fields.MarkupField(help_text=b'you can use <a href="https://daringfireball.net/projects/markdown/basics" rel="nofollow">markdown</a> for formatting here')),
                ('commission_date', models.DateField(help_text=b'when you placed your commission')),
                ('received_date', models.DateField(help_text=b'when you received your costume', null=True, blank=True)),
                ('construction', models.DecimalField(max_digits=2, decimal_places=1)),
                ('communication', models.DecimalField(max_digits=2, decimal_places=1)),
                ('timeliness', models.DecimalField(max_digits=2, decimal_places=1)),
            ],
            options={
                'ordering': [b'-edited'],
            },
            bases=(models.Model,),
        ),
    ]
