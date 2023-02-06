from django.urls import path
from .views import index_page, list_pokes_page, pokemon_detail, register_user


urlpatterns = [
    path('', index_page, name="index_page"),
    path('list_pokes/', list_pokes_page, name="list_pokes_page"),
    path('poke/<slug:slug>/', pokemon_detail, name="pokemon_detail"),
    path('register/', register_user, name="register_user"),
]