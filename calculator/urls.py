from . import views
from django.urls import path


urlpatterns = [
    path('calculator/', views.calc, name='calc'),
    path('run-calc/', views.run_calc, name='run_calc'),
    path('', views.LoadHomePage.as_view()),
    path('home/', views.LoadLoggedInHomepage.as_view(), name='home')
]
