from . import views
from django.urls import path


urlpatterns = [
    #path('', views.calc, name='calc'),
    path('', views.LoadHomePage.as_view())
]
