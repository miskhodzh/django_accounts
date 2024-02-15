from django.urls import path
from django.contrib.auth.views import LogoutView

from . views import Login, Profile, Registration

app_name = 'accounts'
urlpatterns = [
    path('', Profile.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('logout/',
         LogoutView.as_view(next_page='accounts:login'),
         name='logout'
    ),
    path('registration/', Registration.as_view(), name='registration'),
]
