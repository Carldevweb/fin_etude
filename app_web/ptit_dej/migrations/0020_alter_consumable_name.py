# Generated by Django 4.1.2 on 2022-10-28 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptit_dej', '0019_alter_consumable_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumable',
            name='name',
            field=models.CharField(choices=[('pain au choco', 'pain au chocolat'), ('croissant', 'Croissant'), ("jus d'orange", "jus d'orange"), ('jus de pomme', 'Jus de pomme'), ('Café', 'Café'), ('maison', 'maison')], default='Café', max_length=15),
        ),
    ]
