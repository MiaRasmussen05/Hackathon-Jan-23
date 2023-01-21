from . import views
from django.urls import path


urlpatterns = [
    path('calculator/', views.calc, name='calc'),
    path('', views.LoadHomePage.as_view())
]
