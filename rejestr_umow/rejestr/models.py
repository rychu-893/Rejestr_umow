from django.db import models
from django.db import connection
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
#from apscheduler.schedulers.blocking import BlockingScheduler

#from django.utils.safestring import mark_safe
#import datetime
#from django.conf import settings
#from django.contrib.auth.admin import User
#from django.contrib.auth import get_user_model
#from django.core.exceptions import ValidationError
TYP_P = (
    ('L', 'LEKARZ'),
    ('P', 'PIELĘGNIARKA'),
    ('F', 'FIZJOTERAPEUTA'),
    ('Y', 'PSYCHOLOG'),
    ('T', 'TECHNIK STERYLIZACJI MEDYCZNEJ')
)
TYP_U = (
    ('K', 'KONTRAKT'),
    ('Z', 'ZLECENIE')
)


class Kadry_k(models.Model):
    nr_umowy = models.CharField(max_length=30)
    data_podpisania = models.DateField()
    nr_postepowania = models.CharField(max_length=30,null=True, blank=True)
    personel = models.CharField(choices=TYP_P, max_length=1,  default='L')
    typ_umowy = models.CharField(choices=TYP_U, max_length=1,  default='K')
    kontrahent = models.CharField(max_length=255)
    przedmiot = models.CharField(max_length=255)
    od = models.DateField()
    do = models.DateField()
    polisa_oc = models.DateField(null=True,blank=True)
    badania_medyczne = models.DateField(null=True,blank=True)
    załącznik = models.FileField(null=True, blank=True)
    #dodal = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True, default=primary)
    #dodal = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE )

    class Meta:
        verbose_name_plural = 'Kadry'

    def __str__(self):
        return self.nr_umowy




class Kadry_a(models.Model):
    nr_umowy = models.ForeignKey(Kadry_k, on_delete=models.CASCADE)
    nr_aneksu = models.CharField(max_length=30)
    data_podpisania = models.DateField()
    od = models.DateField()
    do = models.DateField()
    załącznik = models.FileField(null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Kadry-aneksy'
    def __str__(self):
        return f'NR_UMOWY:{self.nr_umowy}'


class Sprzedaz(models.Model):
    nr_umowy = models.CharField(max_length=30)
    data_podpisania = models.DateField()
    kontrahent = models.CharField(max_length=255)
    od = models.DateField()
    do = models.DateField()
    załącznik = models.FileField(null=True,blank=True)
    color = models.CharField(max_length=7,null=True)
    class Meta:
        verbose_name_plural = 'Sprzedaż'
    def __str__(self):
        return self.nr_umowy

class Sprzedaz_a(models.Model):
    nr_umowy = models.ForeignKey(Sprzedaz, on_delete=models.CASCADE)
    nr_aneksu = models.CharField(max_length=30)
    data_podpisania = models.DateField()
    od = models.DateField()
    do = models.DateField()
    załącznik = models.FileField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Sprzedaż-aneksy'
    def __str__(self):
        return f'NR_UMOWY:{self.nr_umowy}'

class Zamowienia(models.Model):
    nr_umowy = models.CharField(max_length=30)
    data_podpisania = models.DateField()
    nr_postepowania = models.CharField(max_length=30,null=True, blank=True)
    kontrahent = models.CharField(max_length=255)
    przedmiot = models.CharField(max_length=255)
    od = models.DateField()
    do = models.DateField()
    załącznik = models.FileField(null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Zamówienia Publiczne'

    def __str__(self):
        return self.nr_umowy

class Zamowienia_a(models.Model):
    nr_umowy = models.ForeignKey(Zamowienia, on_delete=models.CASCADE)
    nr_aneksu = models.CharField(max_length=30)
    data_podpisania = models.DateField()
    od = models.DateField()
    do = models.DateField()
    załącznik = models.FileField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Zamówienia-aneksy'
    def __str__(self):
        return f'NR_UMOWY:{self.nr_umowy}'

class Pozostale(models.Model):
    nr_rejestru = models.CharField(max_length=30)
    nr_umowy = models.CharField(max_length=30)
    data_podpisania = models.DateField()
    kontrahent = models.CharField(max_length=255)
    przedmiot = models.CharField(max_length=255)
    od = models.DateField()
    do = models.DateField()
    załącznik = models.FileField(null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Pozostałe'

    def __str__(self):
        return self.nr_umowy

class Zapytania(models.Model):
    nr_umowy = models.CharField(max_length=30)
    data_podpisania = models.DateField()
    nr_postepowania = models.CharField(max_length=30, null=True, blank=True)
    kontrahent = models.CharField(max_length=255)
    przedmiot = models.CharField(max_length=255)
    od = models.DateField()
    do = models.DateField()
    załącznik = models.FileField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Zapytania ofertowe'

    def __str__(self):
        return self.nr_umowy
#class koniec_umow(models.Model):
#    rejestr = models.CharField(max_length=30)
#    nr_umowy = models.CharField(max_length=30)
#    kontrahent = models.CharField(max_length=255)
#    do_konca_umowy = models.DateField()

#    class Meta:
#        managed = False
#        db_table = "koniec_umow"






