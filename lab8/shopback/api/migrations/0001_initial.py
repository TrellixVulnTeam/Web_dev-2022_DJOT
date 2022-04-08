# Generated by Django 2.2 on 2022-04-07 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0)),
                ('description', models.TextField(default='')),
                ('count', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=None)),
            ],
        ),
    ]
