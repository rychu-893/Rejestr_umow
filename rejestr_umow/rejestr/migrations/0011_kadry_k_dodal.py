# Generated by Django 4.1.3 on 2022-12-02 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rejestr', '0010_remove_kadry_k_dodal'),
    ]

    operations = [
        migrations.AddField(
            model_name='kadry_k',
            name='dodal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]