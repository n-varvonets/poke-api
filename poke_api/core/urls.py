from django.urls import path
from .views import index_page, list_pokes_page, pokemon_detail, register_user
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('login', LoginView.as_view(), name="login"),  # when we use a class as view - we have it to indicate
    path('', index_page, name="index_page"),
    path('list_pokes/', list_pokes_page, name="list_pokes_page"),
    path('poke/<slug:slug>/', pokemon_detail, name="pokemon_detail"),
    path('register/', register_user, name="register_user"),
]