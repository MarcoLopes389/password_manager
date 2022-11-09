from django.apps import AppConfig


class PasswordConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'password'

    def ready(self):
        from password.jobs import init_tasks

        init_tasks()
