# Generated by Django 2.2 on 2019-06-07 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('birthYear', models.PositiveSmallIntegerField(help_text="Authors' year of birth")),
                ('facePhoto', models.CharField(help_text="URL to authors' photo", max_length=300)),
            ],
        ),
    ]
