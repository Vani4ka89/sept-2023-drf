# Generated by Django 5.0.4 on 2024-04-30 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('body_type', models.CharField(max_length=30)),
                ('engine', models.FloatField()),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]