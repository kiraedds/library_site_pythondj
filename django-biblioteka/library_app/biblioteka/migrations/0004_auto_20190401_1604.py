# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteka', '0003_remove_bookinstance_imprint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(primary_key=True, max_length=13, serialize=False),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(primary_key=True, default=uuid.uuid4, serialize=False),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(max_length=1, blank=True, default='m', choices=[('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], help_text='Book availability'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(primary_key=True, max_length=200, serialize=False, help_text='gatunek)'),
        ),
    ]
