# Generated by Django 4.0.2 on 2022-04-23 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course_t',
            fields=[
                ('course_ID', models.CharField(db_column='course_id', max_length=7, primary_key=True, serialize=False)),
                ('course_name', models.CharField(blank=True, db_column='course_name', max_length=50, null=True)),
                ('credit_hours', models.IntegerField(blank=True, db_column='credit_hours', null=True)),
            ],
            options={
                'db_table': 'course_t',
            },
        ),
    ]