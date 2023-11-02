from django.contrib import admin
from .models import Kadry_k, Sprzedaz, Kadry_a, Sprzedaz_a, Zamowienia, Zamowienia_a, Pozostale, Zapytania
from import_export.admin import ImportExportModelAdmin
from .form import CategoryForm
from django.db import connection
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.models import User, Group


class Kadry_aInline(admin.TabularInline):
    model = Kadry_a
class Sprzedaz_aInline(admin.TabularInline):
    model = Sprzedaz_a
class Zamowienia_aInline(admin.TabularInline):
    model = Zamowienia_a

@admin.register(Kadry_k)
class Kadry_kAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    #def get_changeform_initial_data(self, request):
    #    get_data = super(Kadry_kAdmin, self).get_changeform_initial_data(request)
    #    get_data['dodal'] = request.user.pk
    #    return get_data
    search_fields = ['kontrahent','nr_umowy']
    list_display = ['id','nr_umowy','data_podpisania','nr_postepowania','personel','typ_umowy','kontrahent','przedmiot','od','do','polisa_oc','badania_medyczne','załącznik']
    list_filter = ['typ_umowy','personel']
    inlines = [
        Kadry_aInline
    ]
    #readonly_fields = ['dodal']

@admin.register(Kadry_a)
class Kadry_aAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nr_umowy','nr_aneksu']
    list_display = ['id','nr_umowy','nr_aneksu','data_podpisania','od','do','załącznik' ]

@admin.register(Sprzedaz)
class SprzedazAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    form = CategoryForm
    #filter_horizontal = ('color',)
    fieldsets = (
        (None, {
            'fields': (('nr_umowy', 'kontrahent'), 'data_podpisania', 'color')
            }),
        )
    search_fields = ['nr_umowy', 'kontrahent']
    list_display = ['id', 'nr_umowy', 'kontrahent','data_podpisania', 'od', 'do', 'załącznik','color']
    inlines = [
        Sprzedaz_aInline
    ]
@admin.register(Sprzedaz_a)
class Sprzedaz_aAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nr_umowy', 'nr_aneksu']
    list_display = ['id', 'nr_umowy', 'nr_aneksu','data_podpisania', 'od', 'do', 'załącznik']

@admin.register(Zamowienia)
class ZamowieniaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nr_umowy', 'kontrahent', 'przedmiot']
    list_display = ['id', 'nr_umowy','data_podpisania', 'nr_postepowania', 'kontrahent','przedmiot', 'od', 'do', 'załącznik']
    inlines = [
        Zamowienia_aInline
    ]
@admin.register(Zamowienia_a)
class Zamowienia_aAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nr_umowy', 'nr_aneksu']
    list_display = ['id', 'nr_umowy', 'nr_aneksu','data_podpisania', 'od', 'do', 'załącznik']

@admin.register(Pozostale)
class PozostaleAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nr_umowy', 'kontrahent', 'przedmiot']
    list_display = ['id', 'nr_umowy','data_podpisania', 'kontrahent','przedmiot', 'od', 'do', 'załącznik']

@admin.register(Zapytania)
class ZapytaniaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nr_umowy', 'kontrahent', 'przedmiot']
    list_display = ['id', 'nr_umowy','data_podpisania', 'nr_postepowania', 'kontrahent','przedmiot', 'od', 'do', 'załącznik']


#@admin.register(koniec_umow)
#class koniec_umow_aAdmin(ImportExportModelAdmin,admin.ModelAdmin):
#   list_display = ['rejestr', 'nr_umowy', 'kontrahent', 'do_konca_umowy']
"""
#recipient_list = User.objects.filter(is_active=True).values_list('email', flat=True)
group = Group.objects.get(name='KADRY')
users = group.user_set.values_list('email', flat=True)
# Pobranie danych z bazy danych za pomocą zapytania SQL
with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM koniec_umow_kadry")
    dane = cursor.fetchall()

# Sformatowanie treści wiadomości za pomocą szablonu HTML
html_message = render_to_string('kadry.html', {'dane': dane})
# Utwórz obiekt wiadomości e-mail
message = EmailMessage(
    subject="Lista umów które wygasają",
    body=html_message,
    from_email="rejestr_umow@ncznamyslow.pl",
    to=users
)
message.content_subtype = "html"

# Wyslij wiadomość
if len(dane) >0:
    message.send()
else:
    pass
################ZAMOWIENIA##############
group = Group.objects.get(name='ZAMOWIENIA')
users = group.user_set.values_list('email', flat=True)
# Pobranie danych z bazy danych za pomocą zapytania SQL
with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM koniec_umow_zam")
    dane = cursor.fetchall()

# Sformatowanie treści wiadomości za pomocą szablonu HTML
html_message = render_to_string('zamowienia.html', {'dane': dane})
# Utwórz obiekt wiadomości e-mail
message = EmailMessage(
    subject="Lista umów które wygasają",
    body=html_message,
    from_email="rejestr_umow@ncznamyslow.pl",
    to=users
)
message.content_subtype = "html"

# Wyslij wiadomość
if len(dane) >0:
    message.send()
else:
    pass

###################SPRZEDAZ####################
group = Group.objects.get(name='SPRZEDAZ')
users = group.user_set.values_list('email', flat=True)
# Pobranie danych z bazy danych za pomocą zapytania SQL
with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM koniec_umow_sprz")
    dane = cursor.fetchall()

# Sformatowanie treści wiadomości za pomocą szablonu HTML
html_message = render_to_string('sprzedaz.html', {'dane': dane})
# Utwórz obiekt wiadomości e-mail
message = EmailMessage(
    subject="Lista umów które wygasają",
    body=html_message,
    from_email="rejestr_umow@ncznamyslow.pl",
    to=users
)
message.content_subtype = "html"

# Wyslij wiadomość
if len(dane) >0:
    message.send()
else:
    pass

###################POZOSTALE####################
group = Group.objects.get(name='POZOSTAŁE')
users = group.user_set.values_list('email', flat=True)
# Pobranie danych z bazy danych za pomocą zapytania SQL
with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM koniec_umow_pozostale")
    dane = cursor.fetchall()

# Sformatowanie treści wiadomości za pomocą szablonu HTML
html_message = render_to_string('pozostale.html', {'dane': dane})
# Utwórz obiekt wiadomości e-mail
message = EmailMessage(
    subject="Lista umów które wygasają",
    body=html_message,
    from_email="rejestr_umow@ncznamyslow.pl",
    to=users
)
message.content_subtype = "html"

# Wyslij wiadomość
if len(dane) >0:
    message.send()
else:
    pass"""