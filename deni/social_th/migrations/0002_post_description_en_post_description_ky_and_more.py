# Generated by Django 5.1.4 on 2024-12-21 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_th', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='hashtag_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='hashtag_ky',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='hashtag_ru',
            field=models.CharField(max_length=150, null=True),
        ),
    ]