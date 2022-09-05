# Generated by Django 4.0.4 on 2022-09-05 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_report_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatsReport1H',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interval5mins', models.IntegerField(db_column='slice1')),
                ('interval10mins', models.IntegerField(db_column='slice2')),
                ('interval15mins', models.IntegerField(db_column='slice3')),
                ('interval20mins', models.IntegerField(db_column='slice4')),
                ('interval25mins', models.IntegerField(db_column='slice5')),
                ('interval30mins', models.IntegerField(db_column='slice6')),
                ('interval35mins', models.IntegerField(db_column='slice7')),
                ('interval40mins', models.IntegerField(db_column='slice8')),
                ('interval45mins', models.IntegerField(db_column='slice9')),
                ('interval50mins', models.IntegerField(db_column='slice10')),
                ('interval55mins', models.IntegerField(db_column='slice11')),
                ('interval60mins', models.IntegerField(db_column='slice12')),
            ],
            options={
                'db_table': ' stats_report_1h',
                'managed': False,
            },
        ),
    ]
