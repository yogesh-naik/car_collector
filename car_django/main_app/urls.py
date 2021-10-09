from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllCars.as_view(), name="All Cars"), # <- here we have added the new path
     path('about/', views.About.as_view(), name="about_page"),
    path('cars/', views.CarsList.as_view(), name="cars_list"),
    path('about/',views.AllCars.as_view(), name="All Cars"),
    # Route for create
    path('cars/new/', views.AddCar_Create.as_view(), name="car_create"),
    
    # Our new Route including the pk param
    path('cars/<int:pk>/', views.CarDetail.as_view(), name="car_detail"),
    path('cars/<int:pk>/update',views.CarUpdate.as_view(), name="car_update"),
    # Our new Route including the pk param
    path('cars/<int:pk>/delete',views.CarDelete.as_view(), name="car_delete"),
    
    #######################
    path('cars/<int:pk>/carmodels/new/',views.CarmodelCreate.as_view(), name="carmodel_create"),
    
    path('cars/carmodels/<int:pk>/delete/',views.CarmodelDelete.as_view(), name="carmodel_delete"),
    
    ################ Sign up
    path('accounts/signup/', views.Signup.as_view(), name="signup")
]