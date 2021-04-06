# Generated by Django 3.1.7 on 2021-04-02 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_symptom'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicineHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_hame', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='symptom',
            name='cough_severity',
            field=models.SmallIntegerField(choices=[(0, 'Never'), (1, 'Almost never'), (2, 'Sometimes'), (3, 'Almost always'), (4, 'Always')]),
        ),
    ]
