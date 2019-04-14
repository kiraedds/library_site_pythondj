# Generated by Django 2.2 on 2019-04-08 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publishers', '0001_initial'),
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('ISBN', models.CharField(max_length=13)),
                ('genre', models.CharField(blank=True, choices=[('FAN', 'Fantasy'), ('SF', 'Science Fiction'), ('WEST', 'Western'), ('ROM', 'Romance'), ('THR', 'Thriller'), ('MYST', 'Mystery'), ('DS', 'Detective Story'), ('MEM', 'Memoir'), ('BIO', 'Biography'), ('PLAY', 'Play'), ('MUS', 'Musical'), ('SAT', 'Satire'), ('HAIKU', 'Haiku'), ('HOR', 'Horror'), ('DIY', 'DIY'), ('DICT', 'Dictionary')], default='Undefined', help_text='Genre of the book', max_length=20)),
                ('cover', models.CharField(max_length=300)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authors.Author')),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='publishers.Publisher')),
            ],
        ),
    ]
