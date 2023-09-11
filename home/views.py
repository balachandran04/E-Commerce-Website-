import json

from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.shortcuts import redirect
from home.form import UserLoginForm
from django.contrib.auth import authenticate,login,logout
from  django.http import JsonResponse




def home(request):
     products = Product.objects.filter(trending=True)
     return render(request, 'home/index.html',{'products': products})


def add_to_cart(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.load(request)
            product_qty = data['product_qty']
            product_id = data['pid']
            # print(request.user.id)
            product_status = Product.objects.get(id=product_id)
            if product_status:
                if Cart.objects.filter(user=request.user.id, product_id=product_id):
                    return JsonResponse({'status': 'Product Already in Cart'}, status=200)
                else:
                    if product_status.quantity >= product_qty:
                        Cart.objects.create(user=request.user, product_id=product_id, product_qty=product_qty)
                        return JsonResponse({'status': 'Product Added to Cart'}, status=200)
                    else:
                        return JsonResponse({'status': 'Product Stock Not Available'}, status=200)
        else:
            return JsonResponse({'status': 'Login to Add Cart'}, status=200)
    else:
        return JsonResponse({'status': 'Invalid Access'}, status=200)
def user_logout(request):
    if request.user.is_authenticated:
       logout(request)
       messages.success(request,'Logout is Successfully')
       return redirect('/')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request == 'POST':
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
            login(request,user)
            messages.success(request,'Logged is Successfully')
            return redirect('home')
        else:
            messages.error(request,"Invalid User name or password")
            return redirect('login')

    return render(request, 'home/login.html')

def register(request):
    form=UserLoginForm()
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration success You can Login Now")
            return redirect('/login')
    return render(request,'home/register.html',{'form': form})
def Collections(request):
    categories = Category.objects.all()
    return render(request, 'home/Collections.html', {'categories': categories})

def Collectionsview(request, name):
    if Category.objects.filter(name=name).exists():
        products = Product.objects.filter(category__name=name)
        return render(request, 'home/products/index.html', {'products': products, 'category_name': name})
    else:
        messages.warning(request, 'No such Category found')
        return redirect('app_name:Collections')
def product_details(request,cname,pname):
    if Category.objects.filter(name=cname):
        if Product.objects.filter(name=pname):
           products = Product.objects.filter(name=pname).first()
           return render(request, 'home/products/product_details.html', {'products': products})
        else:
            messages.error(request,'No such Products found')
            return redirect("Collections")
    else:
        messages.error(request, 'No such Category found')
        return redirect('Collections')






