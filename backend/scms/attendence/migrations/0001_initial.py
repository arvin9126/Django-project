# Generated by Django 3.0.7 on 2020-06-05 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studentclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=50)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendence', models.CharField(max_length=10)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Student')),
                ('studentclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendence.Studentclass')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Teacher')),
            ],
        ),
    ]
