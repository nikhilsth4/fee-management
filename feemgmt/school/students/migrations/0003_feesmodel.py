# Generated by Django 2.0.3 on 2018-10-12 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20181012_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Receipt_no', models.IntegerField()),
                ('Total_fees', models.IntegerField()),
                ('Std_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.StudentModel')),
            ],
        ),
    ]
