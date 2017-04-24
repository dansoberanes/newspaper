# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20170312_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='position',
            field=models.CharField(default='writer', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=tinymce.models.HTMLField(),
        ),
    ]
