# Generated by Django 2.2 on 2021-06-21 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0028_db_project_global_datas'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_project',
            name='encryption',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
