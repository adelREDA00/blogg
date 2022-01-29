# Generated by Django 4.0.1 on 2022-01-26 01:52

from django.db import migrations, models
import tkinter.tix


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=tkinter.tix.Tree, upload_to='images/profile'),
            preserve_default=tkinter.tix.Tree,
        ),
    ]