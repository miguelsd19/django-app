# Generated by Django 3.2.5 on 2022-07-13 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_auto_20220713_2230'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='fav',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='fav',
            name='ad',
        ),
        migrations.RemoveField(
            model_name='fav',
            name='user',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='favorites',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='picture',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Fav',
        ),
    ]