# Generated by Django 3.2.8 on 2021-10-21 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_permission_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='id_user',
        ),
        migrations.DeleteModel(
            name='Permission',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
