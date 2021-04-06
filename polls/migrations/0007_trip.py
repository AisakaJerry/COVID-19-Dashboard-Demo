# Generated by Django 3.1.7 on 2021-04-02 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_surroundingsituation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('departure_date', models.DateField()),
                ('lasting_day', models.IntegerField()),
            ],
        ),
    ]