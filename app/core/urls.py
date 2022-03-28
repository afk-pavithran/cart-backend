from django.urls import path
from .views import index

urlpatterns = [
    path('', name='home', view=index)
]