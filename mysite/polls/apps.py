from django.apps import AppConfig


# Referenced by the project (polls.apps.PollsConfig)
class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
