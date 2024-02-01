from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product
# Create your views here.
def store(request):
    product=Product.objects.all
    paginator = Paginator(product, 6)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    context={
        'product':product,
        # 'page':page_obj,
    }
    return render(request,'pages/store.html',context)