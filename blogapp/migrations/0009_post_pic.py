# Generated by Django 4.0.1 on 2022-01-26 01:55

from django.db import migrations, models
import tkinter.tix


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pic',
            field=models.ImageField(blank=True, null=tkinter.tix.Tree, upload_to='images/'),
            preserve_default=tkinter.tix.Tree,
        ),
    ]
