from unicodedata import name
from django.urls import path
from app.login.views import Login,Logout

urlpatterns = [
    path('/login', Login.as_view(), name='login'),
    path('/logout', Logout.as_view(), name='Logout'),
]
