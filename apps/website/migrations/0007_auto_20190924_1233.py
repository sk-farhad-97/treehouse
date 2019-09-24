# Generated by Django 2.2 on 2019-09-24 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20190924_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(2, 'Service'), (3, 'Project'), (7, 'Type3'), (10, 'Type6'), (8, 'Type4'), (1, 'Quote'), (5, 'Resume'), (0, 'Blog post'), (6, 'Address'), (4, 'About'), (9, 'Type5')], default=0),
        ),
        migrations.AlterField(
            model_name='textfield',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(10, 'Type6'), (0, 'Name'), (5, 'Type1'), (6, 'Type2'), (8, 'Type4'), (7, 'Type3'), (2, 'Email'), (9, 'Type5'), (3, 'Quote'), (1, 'Tagline'), (4, 'Address')], default=0),
        ),
    ]