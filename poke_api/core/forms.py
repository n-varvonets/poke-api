from django.contrib.auth.models import User
from django import forms
from .models import Pokemon

class UserRegistrationFrom(forms.ModelForm):
    # there're two form which we can use:
    #       - forms.Form: you need to specify all fields of your models(name, surname, ...)
    #       - forms.ModelForm: it will create a from according ro your model. so you don't need to specify all fields:
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "first_name", "email")

    def clean_password2(self):
        """check the pass"""
        # print(self, "-\n- ", self.cleaned_data)  # self - всю форму с тегами, self.cleaned_data - вьідаст форму в виде джсона очищенную без тегов
        cd = self.cleaned_data
        if cd['password'] != cd["password2"]:
            raise forms.ValidationError("Password is not matching, hello from {forms.py}")
        return cd["password2"]


class PokemonAddingForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ('name', )


class PokemonUpdatingForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ('name', 'owner_of_poke')
