# Generated by Django 2.0.3 on 2018-06-20 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='direction',
            old_name='direction',
            new_name='faculty',
        ),
        migrations.RenameField(
            model_name='faculty',
            old_name='faculty',
            new_name='name',
        ),
        migrations.AddField(
            model_name='direction',
            name='name',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='direction',
            name='total_result',
            field=models.IntegerField(default=282),
        ),
    ]