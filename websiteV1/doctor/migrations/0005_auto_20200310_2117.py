# Generated by Django 3.0.4 on 2020-03-10 15:47

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_auto_20200310_1850'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='doctor',
            managers=[
                ('value', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='id',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='id',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='did',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
