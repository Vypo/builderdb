# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builders', '0002_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(max_length=2048)),
                ('builder', models.ForeignKey(to='builders.Builder', to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
