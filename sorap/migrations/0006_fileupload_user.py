# Generated by Django 4.0.3 on 2022-11-30 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorap', '0005_remove_fileupload_content_remove_fileupload_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='user',
            field=models.TextField(null=True),
        ),
    ]
