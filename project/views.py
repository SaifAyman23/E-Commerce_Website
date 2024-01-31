from django.shortcuts import render
from category.models import Category
def home(request): 
    category =Category.objects.all
    context={
        'category':category,
    }
    return render(request,'pages/home.html',context)