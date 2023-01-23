from . import views
from django.urls import path


urlpatterns = [
    path('', views.profile, name='profile'),
    path('home/', views.LoadLoggedInHomepage.as_view(), name='home')
]
