# Generated by Django 4.1.3 on 2022-12-01 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rejestr', '0005_kadry_a'),
    ]

    operations = [
        migrations.AddField(
            model_name='kadry_k',
            name='nr_postepowania',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]