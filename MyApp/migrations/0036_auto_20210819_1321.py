# Generated by Django 2.2 on 2021-08-19 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0035_auto_20210819_1035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='db_apis',
            old_name='api_cert',
            new_name='cert',
        ),
        migrations.RenameField(
            model_name='db_apis_log',
            old_name='api_cert',
            new_name='cert',
        ),
        migrations.RenameField(
            model_name='db_step',
            old_name='api_cert',
            new_name='cert',
        ),
    ]