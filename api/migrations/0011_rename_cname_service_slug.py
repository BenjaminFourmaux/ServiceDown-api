# Generated by Django 4.0.4 on 2022-09-30 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_currentstatus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='cname',
            new_name='slug',
        ),
    ]