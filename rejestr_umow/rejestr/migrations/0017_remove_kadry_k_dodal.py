# Generated by Django 4.1.3 on 2022-12-02 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rejestr', '0016_alter_kadry_k_dodal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kadry_k',
            name='dodal',
        ),
    ]
