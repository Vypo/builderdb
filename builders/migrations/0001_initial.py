# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import markupfield.fields
import easy_thumbnails.fields
from django.conf import settings
import builders.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Builder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, validators=[builders.models._validate_builder_name])),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('status', models.CharField(max_length=16, choices=[(b'unknown', b'Unknown'), (b'closed', b'Closed'), (b'quotes', b'Quotes Only'), (b'open', b'Open')])),
                ('banner', easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'headers')),
                ('thumb', easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'thumbs', verbose_name=b'thumbnail')),
                ('description', markupfield.fields.MarkupField(help_text=b'you can use <a href="https://daringfireball.net/projects/markdown/basics" rel="nofollow">markdown</a> for formatting here', blank=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name=b'members')),
            ],
            options={
                'ordering': [b'name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'photos')),
                ('caption', models.CharField(max_length=1024)),
                ('priority', models.IntegerField(default=0, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', to_field='id')),
                ('object_id', models.PositiveIntegerField()),
            ],
            options={
                'ordering': [b'-priority', b'-edited'],
            },
            bases=(models.Model,),
        ),
    ]
