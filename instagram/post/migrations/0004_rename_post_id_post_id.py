# Generated by Django 3.2.5 on 2021-08-31 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_rename_id_post_post_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_id',
            new_name='id',
        ),
    ]
