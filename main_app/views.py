from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Wine, Food, Photo
from .forms import YearForm

# Add the following import
from django.http import HttpResponse

import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'winecollector'

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def wines_index(request):
    wines = Wine.objects.all() 
    return render(request, 'wines/index.html', { 'wines': wines })

def wines_detail(request, wine_id):
    wine = Wine.objects.get(id=wine_id)
    foods_wine_doesnt_have = Food.objects.exclude(id__in = wine.foods.all().values_list('id'))
    year_form = YearForm()
    return render(request, 'wines/detail.html', { 
        'wine': wine, 'year_form':year_form,
        'foods': foods_wine_doesnt_have
    })

def add_year(request, wine_id):
    form = YearForm(request.POST)
    # validate the form
    if form.is_valid():
        new_year = form.save(commit=False)
        new_year.wine_id = wine_id
        new_year.save()
    return redirect('detail', wine_id=wine_id)

class WineCreate(CreateView):
    model = Wine
    fields = ['name', 'winetype', 'cost']
    success_url = '/wines/'

class WineUpdate(UpdateView):
    model = Wine
    fields = ['winetype', 'cost']

class WineDelete(DeleteView):
    model = Wine
    success_url = '/wines/'


def foods_index(request):
    foods = Food.objects.all()
    context = {'foods': foods}
    
    return render(request, 'food/index.html', context)

def food_detail(request, food_id):
    food = Food.objects.get(id=food_id)
    context = {
        'food': food
    }
    return render(request, 'food/detail.html', context)
    
class Create_Food(CreateView):
    model = Food
    fields = '__all__'

class Delete_food(DeleteView):
    model = Food
    success_url = '/foods/'     

def assoc_food(request, wine_id, food_id):
    Wine.objects.get(id=wine_id).foods.add(food_id)
    return redirect('detail', wine_id=wine_id)

def remove_food(request, wine_id, food_id):
    Wine.objects.get(id=wine_id).foods.remove(food_id)
    return redirect('detail', wine_id=wine_id)

def add_photo(request, wine_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, wine_id=wine_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', wine_id=wine_id)