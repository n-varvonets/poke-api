from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Pokemon
from .forms import UserRegistrationFrom, PokemonAddingForm
# Create your views here.


def index_page(request):
    # return HttpResponse("Welcome to index page")
    base_html_variable_for_index = "base_html_variable_for_index_from_VIEW"
    return render(request, "base.html", {"base_html_variable_for_index": base_html_variable_for_index})


def list_pokes_page(request):
    # return HttpResponse("Welcome to index page")
    hardcore_list_of_pokes = "Slow-Nick-Poke-Welcome from google"
    list_of_pokes = Pokemon.objects.all().order_by("name")
    # list_of_pokes = get_object_or_404(Pokemon)
    return render(request, "list_poks.html", {"hardcore_list_of_pokes": hardcore_list_of_pokes, "list_of_pokes": list_of_pokes})


def pokemon_detail(request, slug):
    pokemon = get_object_or_404(Pokemon, slug=slug)
    return render(request, 'details.html', {"pokemon": pokemon})


def register_user(request):
    if request.method == "POST":
        user_form = UserRegistrationFrom(request.POST)

        # check received form from client with answer of creating form and fill all required fields
        if user_form.is_valid():
            # create new user object, but we don't want to save that
            # before need to check password
            new_user = user_form.save(commit=False)

            # set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])  # to check password by custom method of RegisterFromUser

            # and now after valid form and password we can save it
            new_user.save()
            return render(request, "account/register_done.html", {"user_form": user_form})
    else:
        user_form = UserRegistrationFrom()  # just empty a new form
    # if npt method post and not valid form with passw - return base reg form
    return render(request, "account/register.html", {"user_form": user_form})


def pokemon_adding_form(request):
    pokemon_form = PokemonAddingForm(request.POST)

    if request.method == "POST":
        if pokemon_form.is_valid():  # we have all fields in appropriate type
            # in this we need to save the data by creating a new pokemon
            pokemon = pokemon_form.save(commit=False)
            pokemon.owner_of_poke = request.user  # по здаумке, тот кто создает нового покемона - тот и будет его владельцем
            pokemon = pokemon_form.save()
            return redirect('list_pokes_page')

    else:
        # если по урл формьі бьіл использован другой методо - возращаем просто пустую форму
        pokemon_form = PokemonAddingForm()
    return render(request, 'account/add_pokemon.html', {"pokemon_form": pokemon_form})

