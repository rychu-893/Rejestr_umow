# Generated by Django 4.1.3 on 2022-12-02 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rejestr', '0013_alter_kadry_k_dodal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kadry_k',
            name='dodal',
            field=models.OneToOneField(blank=True, default='U', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
