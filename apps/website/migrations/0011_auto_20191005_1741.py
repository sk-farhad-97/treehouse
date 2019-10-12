# Generated by Django 2.2 on 2019-10-05 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20191005_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/para_images/'),
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(9, 'Type5'), (8, 'Type4'), (1, 'Quote'), (3, 'Project'), (0, 'Normal'), (10, 'Type6'), (2, 'Service'), (4, 'About'), (6, 'Address'), (7, 'Type3'), (5, 'Short-Bio')], default=0),
        ),
        migrations.AlterField(
            model_name='textfield',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(9, 'Type5'), (3, 'Quote'), (1, 'Tagline'), (2, 'Email'), (10, 'Type6'), (8, 'Type4'), (0, 'Name'), (4, 'Address'), (6, 'Type2'), (5, 'Type1'), (7, 'Type3')], default=0),
        ),
    ]