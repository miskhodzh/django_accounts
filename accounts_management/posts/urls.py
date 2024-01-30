from django.urls import path
from . views import post_create

app_name = 'posts'
urlpatterns = [
    path('create/', post_create, name='post_create')
]