from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import TemplateView, View
# This will import the class we are extending 
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import DetailView
#### For Login
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# For Authorization
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from . models import CarManufacturer ,Carmodel

# Create your views here.
class AllCars(TemplateView):
    template_name = "home.html"
    
class About(TemplateView):
    template_name = "about_page.html"
#  #This is constructor
# class CarManufacturer:
#     def __init__(self, name, logo, Information):
#         self.name = name
#         self.logo = logo
#         self.Information = Information
        
#controller
@method_decorator(login_required, name='dispatch')
class CarsList(TemplateView):
    template_name = "cars_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["all_Cars"] = CarManufacturer.objects.filter(name__icontains=name,user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["all_Cars"] = CarManufacturer.objects.filter(user=self.request.user)
            context["header"] = "Top USA Car Manufacturer"
        return context
    
class AddCar_Create(CreateView):
    model = CarManufacturer
    fields = ['name', 'logo', 'information']
    template_name = "car_create.html"
    # success_url = "/cars/"  #redirect path
    # This is our new method that will add the user into our submitted form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddCar_Create, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('car_detail', kwargs={'pk': self.object.pk})
    
    
class CarDetail(DetailView):
    model = CarManufacturer
    template_name = "car_detail.html"
    
class CarUpdate(UpdateView):
    model = CarManufacturer
    fields = ['name', 'logo', 'information']
    template_name = "car_update.html"
    success_url = "/cars/"  #redirect path
    
    
class CarDelete(DeleteView):
    model = CarManufacturer
    template_name = "car_delete.html"
    success_url = "/cars/" #redirect path
    
######################################################    
class CarmodelCreate(View):
    def post(self, request, pk):
        modelname = request.POST.get("modelname")
        image = request.POST.get("image")
        make = CarManufacturer.objects.get(pk=pk)
        Carmodel.objects.create(modelname=modelname, image=image, make=make)
        return redirect('car_detail', pk=pk)
    
# class CarmodelDelete(DeleteView):
#     def delete(self,pk):
#         context ={}
#         # fetch the object related to passed id
#         obj = get_object_or_404(Carmodel, pk = pk)
#         obj.delete()
#         return redirect('car_detail', pk=pk)

class CarmodelDelete(DeleteView):
    model = Carmodel
    template_name = "carmodel_delete.html"
    success_url = "/cars/" #redirect path
    
    
class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("cars_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)