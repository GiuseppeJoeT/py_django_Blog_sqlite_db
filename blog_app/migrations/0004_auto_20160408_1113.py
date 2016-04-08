# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_post_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='images', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
