# Generated by Django 3.1.7 on 2021-04-02 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20210402_0428'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurroundingSituation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positive_people_name', models.CharField(max_length=20)),
                ('last_meet_date', models.DateField()),
            ],
        ),
    ]
