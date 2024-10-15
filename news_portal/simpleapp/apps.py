from django.apps import AppConfig


class SimpleappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'simpleapp'


class SimpleappConfig(AppConfig):
    name = 'simpleapp'

    def ready(self):
        from .apscheduler import start
        start()
