# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteka', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(primary_key=True, default=uuid.uuid4, serialize=False, help_text='Unique ID for this particular book across whole library'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='biblioteka.Book'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='due_back',
            field=models.DateField(blank=True, null=True),
        ),
    ]
