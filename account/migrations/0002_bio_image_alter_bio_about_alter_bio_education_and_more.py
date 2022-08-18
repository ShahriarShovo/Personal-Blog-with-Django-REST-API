# Generated by Django 4.0.4 on 2022-08-11 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bio',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_image'),
        ),
        migrations.AlterField(
            model_name='bio',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bio',
            name='education',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bio',
            name='profession',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
