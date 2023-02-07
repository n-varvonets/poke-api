from django.urls import path
from .views import index_page, list_pokes_page, pokemon_detail, register_user, pokemon_adding_form, update_pokemon, delete_poke
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView


urlpatterns = [

    path('login', LoginView.as_view(), name="login"),  # when we use a class as view - we have it to indicate
    path('', index_page, name="index_page"),
    path('list_pokes/', list_pokes_page, name="list_pokes_page"),
    path('pokemon_add/', pokemon_adding_form, name="pokemon_adding_form"),
    path('update_pokemon/<slug:slug>', update_pokemon, name="update_pokemon"),  # for updating poke need to indicate which one by passing slug
    path('delete_pokemon/<slug:slug>', delete_poke, name="delete_pokemon"),
    path('poke/<slug:slug>/', pokemon_detail, name="pokemon_detail"),
    path('register/', register_user, name="register_user"),
    path('logout/', LogoutView.as_view(), name="logout"),  # look forward - you have to exactly name logged_out.html : django will be looking for him
    path('password-change/', PasswordChangeView.as_view(), name="password-change"),  # as we use Django build-in registration form we have to fallow rule:
    #  - all identical names in templates/registration as I named
    path('password-change/done/', PasswordChangeDoneView.as_view(), name="password_change_done"),
]
