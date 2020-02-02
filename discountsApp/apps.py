from django.apps import AppConfig


class DiscountsappConfig(AppConfig):
    name = 'discountsApp'

    def ready(self):
        import discountsApp.signals