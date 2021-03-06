# Generated by Django 2.2 on 2019-09-24 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20190914_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(8, 'Type4'), (3, 'Project'), (4, 'About'), (10, 'Type6'), (1, 'Quote'), (0, 'Blog post'), (9, 'Type5'), (6, 'Address'), (2, 'Service'), (5, 'Resume'), (7, 'Type3')], default=0),
        ),
        migrations.AlterField(
            model_name='textfield',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Name'), (2, 'Email'), (10, 'Type6'), (1, 'Tagline'), (6, 'Type2'), (9, 'Type5'), (4, 'Address'), (8, 'Type4'), (5, 'Type1'), (7, 'Type3'), (3, 'Quote')], default=0),
        ),
    ]
