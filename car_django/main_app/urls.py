from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllCars.as_view(), name="All Cars"), # <- here we have added the new path
    path('artists/', views.CarsList.as_view(), name="artist_list"),
]