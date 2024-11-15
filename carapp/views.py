from django.shortcuts import render, get_object_or_404, redirect
from .models import Cars
from .forms import CarForm
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')
# List View - Display all cars
def car_list(request):
    cars = Cars.objects.all()  # Retrieve all car objects
    return render(request, 'car_list.html', {'cars': cars})

# Detail View - Display a single car's details
def car_detail(request, pk):
    car = get_object_or_404(Cars, pk=pk)  # Retrieve car by primary key
    return render(request, 'car_detail.html', {'car': car})

# Create View - Add a new car
def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Car added successfully!")
            return redirect('car_list')  # Redirect to car list view
    else:
        form = CarForm()
    return render(request, 'car_form.html', {'form': form, 'title': 'Add Car'})

# Update View - Edit an existing car
def car_update(request, pk):
    car = get_object_or_404(Cars, pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            messages.success(request, "Car updated successfully!")
            return redirect(reverse('car_detail', args=[pk]))
    else:
        form = CarForm(instance=car)
    return render(request, 'car_form.html', {'form': form, 'title': 'Edit Car'})

def car_delete(request, pk):
    if request.method == 'DELETE':
        car = get_object_or_404(Cars, pk=pk)
        car.delete()
        return JsonResponse({'message': 'Car deleted successfully.'}, status=200)
    return JsonResponse({'message': 'Invalid request method.'}, status=400)