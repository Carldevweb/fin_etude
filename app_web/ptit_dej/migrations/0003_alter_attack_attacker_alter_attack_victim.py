# Generated by Django 4.1.1 on 2022-09-29 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ptit_dej', '0002_attack_consumable_flag_petitdej_tomorrowteam_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attack',
            name='attacker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attack_ransom', to='ptit_dej.tomorrowteam'),
        ),
        migrations.AlterField(
            model_name='attack',
            name='victim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='victim_pay', to='ptit_dej.tomorrowteam'),
        ),
    ]
