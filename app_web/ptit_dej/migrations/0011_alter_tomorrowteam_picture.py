# Generated by Django 4.1.1 on 2022-10-12 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptit_dej', '0010_alter_tomorrowteam_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tomorrowteam',
            name='picture',
            field=models.ImageField(height_field='150', null=True, upload_to='image_profile', width_field='150'),
        ),
    ]
