# Generated by Django 3.1.7 on 2021-04-12 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='localData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('population', models.IntegerField()),
                ('cases', models.IntegerField()),
                ('death', models.IntegerField()),
            ],
        ),
    ]
