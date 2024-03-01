from django.shortcuts import render,redirect
from .models import Product
from .form import ProductForm

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request,'gallery/index.html',{'products':products})


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