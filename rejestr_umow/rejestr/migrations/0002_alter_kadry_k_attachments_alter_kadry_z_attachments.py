# Generated by Django 4.1.3 on 2022-11-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rejestr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kadry_k',
            name='attachments',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='kadry_z',
            name='attachments',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
