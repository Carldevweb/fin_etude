# Generated by Django 4.1.1 on 2022-10-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptit_dej', '0006_alter_tomorrowteam_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tomorrowteam',
            name='password',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
