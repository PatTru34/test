from django.urls import path

from . import views

urlpatterns = [
    path('osoby/', views.osoba_list),
    path('osoby/<int:pk>/', views.osoba_detail),
    path('osoby/<str:imie>/', views.osoba_list_by_name),
    path('stanowiska/', views.stanowisko_list),
    path('stanowiska/<int:pk>', views.stanowisko_detail),

]