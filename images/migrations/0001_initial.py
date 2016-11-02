# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, blank=True)),
                ('url', models.URLField()),
                ('image', models.ImageField(upload_to=b'images/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('total_likes', models.PositiveIntegerField(default=0, db_index=True)),
                ('user', models.ForeignKey(related_name='images_created', to=settings.AUTH_USER_MODEL)),
                ('users_like', models.ManyToManyField(related_name='images_liked', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
    ]
