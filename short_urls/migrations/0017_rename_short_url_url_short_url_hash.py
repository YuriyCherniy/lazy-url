# Generated by Django 3.2.14 on 2022-08-08 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('short_urls', '0016_alter_url_user_ip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='short_url',
            new_name='short_url_hash',
        ),
    ]
