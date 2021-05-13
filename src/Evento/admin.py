from django.contrib import admin
from django.apps import apps
# Register your models here.
models = apps.get_models()
for model in models:
    if not ('GestorTemplates' in str(model)) :
        try:
            admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            pass