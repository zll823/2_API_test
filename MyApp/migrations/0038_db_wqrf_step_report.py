# Generated by Django 2.2 on 2022-03-25 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0037_db_cases_concurrent'),
    ]

    operations = [
        migrations.CreateModel(
            name='DB_wqrf_step_report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_id', models.CharField(default='', max_length=10)),
                ('request_data', models.TextField(default='{}')),
                ('response', models.TextField(default='')),
                ('assert_result', models.CharField(default='{}', max_length=500)),
            ],
        ),
    ]
