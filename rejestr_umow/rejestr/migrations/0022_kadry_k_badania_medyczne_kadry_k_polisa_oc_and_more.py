# Generated by Django 4.1.3 on 2023-02-24 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rejestr', '0021_zapytania'),
    ]

    operations = [
        migrations.AddField(
            model_name='kadry_k',
            name='badania_medyczne',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kadry_k',
            name='polisa_oc',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kadry_k',
            name='personel',
            field=models.CharField(choices=[('L', 'LEKARZ'), ('P', 'PIELĘGNIARKA'), ('F', 'FIZJOTERAPEUTA'), ('Y', 'PSYCHOLOG'), ('T', 'TECHNIK STERYLIZACJI MEDYCZNEJ')], default='L', max_length=1),
        ),
    ]
