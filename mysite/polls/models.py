from django.db import models

MONTHS = models.IntegerChoices('Miesiace',
                               'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

SHIRT_SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
)

PLEC = (
    ('M', 'Mezczyzna'),
    ('K', 'Kobieta'),
    ('I', 'Inne'),
)

class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)


class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=60, null=False, blank=False)
    opis = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return f"{self.nazwa}"


class Osoba(models.Model):
    # PLEC = (
    #     ('M', 'Mezczyzna'),
    #     ('K', 'Kobieta'),
    #     ('I', 'Inne'),
    # )
    imie = models.CharField(max_length=60, null=False, blank=False)
    nazwisko = models.CharField(max_length=60, null=False, blank=False)
    plec = models.CharField(max_length=1, choices=PLEC)
    stanowisko = models.ForeignKey(Stanowisko, on_delete=models.CASCADE)
    data_dodania = models.DateField(null=True, auto_now_add=True)

    class Meta:
        ordering = ["nazwisko"]
    def __str__(self):
        return self.imie+ " " +self.nazwisko
