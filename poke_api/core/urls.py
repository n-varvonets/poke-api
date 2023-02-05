from django.urls import path
from .views import index_page, list_pokes_page


urlpatterns = [
    path('', index_page, name="index_page"),
    path('list_pokes/', list_pokes_page, name="list_pokes_page"),
]