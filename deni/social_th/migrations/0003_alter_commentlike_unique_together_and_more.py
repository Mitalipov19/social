# Generated by Django 5.1.4 on 2024-12-23 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_th', '0002_post_description_en_post_description_ky_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='commentlike',
            unique_together={('user', 'comment')},
        ),
        migrations.AlterUniqueTogether(
            name='postlike',
            unique_together={('user', 'post')},
        ),
    ]
