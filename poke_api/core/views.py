from django.shortcuts import render, HttpResponse, get_list_or_404
from .models import Pokemon
# Create your views here.


def index_page(request):
    # return HttpResponse("Welcome to index page")
    base_html_variable_for_index = "base_html_variable_for_index_from_VIEW"
    return render(request, "base.html", {"base_html_variable_for_index": base_html_variable_for_index})


def list_pokes_page(request):
    # return HttpResponse("Welcome to index page")
    hardcore_list_of_pokes = "Slow-Nick-Poke-Welcome from google"
    list_of_pokes = Pokemon.objects.all().order_by("name")
    return render(request, "list_poks.html", {"hardcore_list_of_pokes": hardcore_list_of_pokes, "list_of_pokes": list_of_pokes})


def pokemon_detail(request, slug):
    list_of_a_poks = get_list_or_404(Pokemon, slug=slug)
    return render(request, 'details.html', {"pokemon": list_of_a_poks[0]})