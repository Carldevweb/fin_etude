# Generated by Django 4.1.1 on 2022-09-29 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ptit_dej', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_attack', models.IntegerField(default=1)),
                ('succesful', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Consumable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('PAC', 'pain au chocolat'), ('CRO', 'Croissant'), ('JDO', "jus d'orange"), ('JDP', 'Jus de pomme'), ('COO', 'Café')], default='COO', max_length=3)),
                ('quantites', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=40)),
                ('used', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('offensive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ptit_dej.attack')),
            ],
        ),
        migrations.CreateModel(
            name='PetitDej',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('created_at', models.DateTimeField()),
                ('consumable', models.ManyToManyField(to='ptit_dej.consumable')),
                ('onslaught', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PetitDej_Pay', to='ptit_dej.attack')),
            ],
        ),
        migrations.CreateModel(
            name='TomorrowTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=12)),
                ('picture', models.ImageField(null=True, upload_to=None)),
            ],
        ),
        migrations.DeleteModel(
            name='tomorrow_team',
        ),
        migrations.AddField(
            model_name='petitdej',
            name='payer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ptit_dej.tomorrowteam'),
        ),
        migrations.AddField(
            model_name='flag',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ptit_dej.tomorrowteam'),
        ),
        migrations.AddField(
            model_name='attack',
            name='attacker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attack_bim', to='ptit_dej.tomorrowteam'),
        ),
        migrations.AddField(
            model_name='attack',
            name='victim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='victim_hello', to='ptit_dej.tomorrowteam'),
        ),
    ]
