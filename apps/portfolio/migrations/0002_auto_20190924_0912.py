# Generated by Django 2.2 on 2019-09-24 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='body_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workhistory',
            name='body_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]