from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        #  импортируем сигнал создания флага, которьій потом передадим в __init__ для работьі
        import core.signals