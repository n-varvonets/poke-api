from django.db import models
from django.contrib.auth.models import User


class Pokemon(models.Model):
    """
    Создадим нашего покемона, которому присвоем его владельца(нашего зарегонного клмента)
    Владелец у покемона может бьіть только один
    """
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=25, unique=True)


    # image = # sprites.other.official-artwork.front_default
    # abilities =  #  abilities: (list)
    # #                   - ability.name
    # types =  #  types: (list)
    # #                   - type.name
    # weight = #weight

    # published = models.DateTimeField(auto_now_add=True)

    print("Explanation of O2O, O2M=FK, M2M and on_delete")
    # owner = models.OneToOneField(User, on_delete=models.)  # One User and he has One Pokemon (Я_и_ДЕВУШКА верньіе)
    owner_of_poke = models.ForeignKey(User, on_delete=models.CASCADE)  # One User and he has Many Pokemons.
    # on_delete=models.CASCADE - if we want to delete an Owner of client this means the Pokemon will be also erased.
    # Pokemon can change an owner in any time.

    # 1) а как сделать тогда что б у одного нашего Юзера бьіло много покемнов,
    #               ПРИ том что бьі єти покемоньі бьіли уникальньі для нашего Юера, т.е. что бьі покеменьі не бьіли у других?
    # Решение: DoreignKey=One2Many(ВЕРНЬІЕ ДЕВУШКИ, Я - БАБНИК)
    # 2) Соответсвенно Many2Many(ШЛЮХА, Я - БАБНИК):
    #               - у одного нашего Юзера бьіло много покемнов,
    #               - покеменьі могуть иметь своих Юезров, и я не у них не один
