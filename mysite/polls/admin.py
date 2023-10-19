from django.contrib import admin

from .models import Person,Team,Osoba,Stanowisko

class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko','plec','idstan']
    list_filter = ['stanowisko']

    @admin.display(description="id")
    def idstan(self,obj):
        return f"{obj.stanowisko} ({obj.stanowisko.id})"


admin.site.register(Person)
admin.site.register(Team)
admin.site.register(Stanowisko)
admin.site.register(Osoba, OsobaAdmin)

