from django.urls import path
from .views import create_inscricao

app_name = 'Inscricao'

urlpatterns = [

    path('create/', create_inscricao, name='create_inscricao'),
]