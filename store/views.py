from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Max,Min
from .models import Product
# Create your views here.
def store(request):
    price_min = Product.objects.all().aggregate(Min('price'))
    price_max = Product.objects.all().aggregate(Max('price'))
    FilterPrice = request.GET.get('FilterPrice')
    if FilterPrice:
        Int_FilterPrice = int(FilterPrice)
        products = Product.objects.filter(price__lte = Int_FilterPrice,is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True)
    paginator = Paginator(products,6) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    print(price_min)
    print(price_max)
    context = {
        'products' : page_obj,
        'price_min' : price_min,
        'price_max' : price_max,
        'FilterPrice':FilterPrice,
    }
    return render(request,'pages/store.html',context)