# Generated by Django 4.2.2 on 2023-07-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_album_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='длительность трека'),
        ),
    ]
