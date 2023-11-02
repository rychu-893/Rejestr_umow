# Generated by Django 4.1.3 on 2022-12-09 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rejestr', '0017_remove_kadry_k_dodal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprzedaz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr_umowy', models.CharField(max_length=30)),
                ('data_podpisania', models.DateField()),
                ('kontrahent', models.CharField(max_length=255)),
                ('od', models.DateField()),
                ('do', models.DateField()),
                ('załącznik', models.FileField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Sprzedaż',
            },
        ),
        migrations.CreateModel(
            name='Sprzedaz_a',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr_aneksu', models.CharField(max_length=30)),
                ('data_podpisania', models.DateField()),
                ('od', models.DateField()),
                ('do', models.DateField()),
                ('załącznik', models.FileField(blank=True, null=True, upload_to='')),
                ('nr_umowy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rejestr.sprzedaz')),
            ],
            options={
                'verbose_name_plural': 'Sprzedaż-aneksy',
            },
        ),
        migrations.DeleteModel(
            name='Kadry_z',
        ),
        migrations.AlterModelOptions(
            name='kadry_a',
            options={'verbose_name_plural': 'Kadry-aneksy'},
        ),
        migrations.AlterModelOptions(
            name='kadry_k',
            options={'verbose_name_plural': 'Kadry'},
        ),
    ]