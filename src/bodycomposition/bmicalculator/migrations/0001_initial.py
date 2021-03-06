# Generated by Django 2.2 on 2019-04-23 03:26

from django.db import migrations, models
import django.db.models.deletion
import django_utils.choices


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('gender', models.CharField(choices=[('m', django_utils.choices.Choice('m', 'Male')), ('f', django_utils.choices.Choice('f', 'Female'))], max_length=1)),
                ('DOB', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Measurements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_kg', models.FloatField()),
                ('height_meters', models.FloatField()),
                ('chest', models.FloatField(null=True)),
                ('axilla', models.FloatField(null=True)),
                ('triceps', models.FloatField(null=True)),
                ('subscapular', models.FloatField(null=True)),
                ('abdomen', models.FloatField(null=True)),
                ('suprailiac', models.FloatField(null=True)),
                ('thigh', models.FloatField(null=True)),
                ('results', models.FloatField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmicalculator.Person')),
            ],
        ),
    ]
