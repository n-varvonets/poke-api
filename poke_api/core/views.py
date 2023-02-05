from django.shortcuts import render, HttpResponse

# Create your views here.

def index_page(request):
    # return HttpResponse("Welcome to index page")
    base_html_variable_for_index = "base_html_variable_for_index_from_VIEW"
    return render(request, "base.html", {"base_html_variable_for_index": base_html_variable_for_index})

def list_pokes_page(request):
    # return HttpResponse("Welcome to index page")
    hardcore_list_of_pokes = "Slow-Nick-Poke"
    return render(request, "list_poks.html", {"hardcore_list_of_pokes": hardcore_list_of_pokes})