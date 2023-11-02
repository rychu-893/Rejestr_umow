# Generated by Django 4.1.3 on 2022-12-12 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rejestr', '0019_zamowienia_zamowienia_a'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pozostale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr_rejestru', models.CharField(max_length=30)),
                ('nr_umowy', models.CharField(max_length=30)),
                ('data_podpisania', models.DateField()),
                ('kontrahent', models.CharField(max_length=255)),
                ('przedmiot', models.CharField(max_length=255)),
                ('od', models.DateField()),
                ('do', models.DateField()),
                ('załącznik', models.FileField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Pozostałe',
            },
        ),
    ]