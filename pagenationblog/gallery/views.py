from django.shortcuts import render,redirect
from .models import Product
from .form import ProductForm
from django.core.paginator import Paginator

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    p = Paginator(products,3)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    return render(request,'gallery/index.html',{'page_obj':page_obj})


def product_details(request,id):
    product = Product.objects.get(id=id)
    return render(request,'gallery/details.html',{'product':product})

def product_delete(request,id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request,'gallery/delete.html',{'product':product})


def edit_product(request,id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    form = ProductForm(instance = product)
    return render(request,'gallery/edit.html',{'form':form})