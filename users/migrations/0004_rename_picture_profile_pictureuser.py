# Generated by Django 3.2 on 2021-05-07 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_delete_example'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='picture',
            new_name='pictureUser',
        ),
    ]
