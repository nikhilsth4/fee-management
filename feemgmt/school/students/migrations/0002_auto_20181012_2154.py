# Generated by Django 2.0.3 on 2018-10-12 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='Std_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
