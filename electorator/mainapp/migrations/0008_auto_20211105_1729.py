# Generated by Django 3.2.8 on 2021-11-05 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20211105_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uik',
            name='num_tik',
        ),
        migrations.AddField(
            model_name='uik',
            name='num_tik',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='mainapp.tik'),
        ),
    ]
