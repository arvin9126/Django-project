# Generated by Django 3.0.7 on 2020-06-06 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20200606_2354'),
        ('exam', '0002_auto_20200606_2354'),
        ('attendence', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='studentclass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Studentclass'),
        ),
        migrations.DeleteModel(
            name='Studentclass',
        ),
    ]
