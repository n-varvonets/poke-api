# - There are different ways that you can create dynamic slacks in Django /
# Существуют различные способы создания динамических слайсов в Django.

# - Dispatcher helps decoupled applications get notified when actions occur elsewhere in the framework /
# Диспетчер помогает разобщенным приложениям получать уведомления о действиях, происходящих в других местах фреймворка.

# - In a nutshell, signals allow certain senders to need to find a set of receivers that some action has taken place. /
# В двух словах, сигналы позволяют определенным отправителям сообщать набору получателей о том, что произошло какое-то действие.

# - They're especially useful when money pieces of code may be interested in the same events /
# Они особенно полезны, когда денежные части кода могут быть заинтересованы в одних и тех же событиях


from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Pokemon
from django.utils.text import slugify


@receiver(pre_save, sender=Pokemon)
def add_slug(sender, instance, *args, **kwargs):
    if instance and not instance.slug:  # if we have created instance(not saved yet) without the slug
        # so autofill the slug
        slug = slugify(instance.name)  # create a slug according pokemon name
        instance.slug = slug


"""Example creating a new Poke with dynamic slug from shell(not admin page)"""
# python3 manage.py shell
# Python 3.9.6 (default, Aug  5 2022, 15:21:02)
# [Clang 14.0.0 (clang-1400.0.29.102)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from django.contrib.auth import get_user_model
# >>> users = get_user_model()
# >>> first_user = users.objects.first()
# >>> print(first_user)  # admin_nick
# >>> from core.models import Pokemon
# >>> new_poke = Pokemon(name='auto_slugged_poke',owner_of_poke=first_user)
# >>> new_poke.save()



