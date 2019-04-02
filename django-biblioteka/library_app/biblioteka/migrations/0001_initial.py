# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(max_length=1000, help_text='Enter a brief description of the book')),
                ('isbn', models.CharField(primary_key=True, max_length=13, serialize=False, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('name', models.CharField(primary_key=True, max_length=200, serialize=False, help_text='Enter a book genre (e.g. Science Fiction)')),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('book', models.ForeignKey(primary_key=True, serialize=False, to='biblioteka.Book')),
                ('imprint', models.CharField(max_length=200)),
                ('due_back', models.DateField(blank=True)),
                ('status', models.CharField(max_length=1, blank=True, default='m', choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], help_text='Book availability')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='biblioteka.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this book', to='biblioteka.Genre'),
        ),
        migrations.AlterUniqueTogether(
            name='author',
            unique_together=set([('first_name', 'last_name', 'date_of_birth')]),
        ),
    ]
