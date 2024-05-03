from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authlogin,logout as userlogout
from django.contrib.auth.decorators import login_required as loginreq
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages

# Create your views here.
@loginreq(login_url='login')
def home(request):
    return render(request,'home.html')

def hf(request):
    return render(request,'hf.html')

def login(request):
    if request.method=="POST":
        fname=request.POST.get('uname')
        password=request.POST.get('password')
        user=authenticate(request,username=fname,password=password)     
        if user is not None:
            authlogin(request,user)
            return redirect('home')
        else:
            messages.error(request, "Username or Password is incorrect...")
            return redirect('login')

    return render(request,'login.html')


def signup(request):
    global uname
    if request.method=="POST":
        fname=request.POST.get('FirstName')
        lname=request.POST.get('LastName')
        uname=fname+" "+lname
        email=request.POST.get('Email')
        password=request.POST.get('Password')
        repassword=request.POST.get('RePassword')
        if password!=repassword:
            return HttpResponse("Password and Conform Password must be same")
        else:
            my_user=User.objects.create_user(uname,email,password)
            my_user.save()
            return redirect('login')

    return render(request,'signup.html')


def logout(request):
    userlogout(request)
    return redirect('login')



@login_required(login_url='/login')
def show(request):
    product=Product.object.all()
    if request.GET.get('search'):
        print (request.GET.get('search'))
        product=product.filter(name_icontainer=request.GET.get('search'))

    products= {'product': product}
    return render(request, 'main.html',products)

def Collections(request):
    category = Category.objects.filter(status=0)
    context= {'category':category}
    return render(request, 'Collections.html', context)

def Collectionsview(request,slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products=Product.objects.filter(category__slug=slug)
        category=Category.objects.filter(slug=slug).first()
        context={'products': products, 'category': category}
        return render(request, 'products/index.html', context)
    else:
        messages.warning(request, 'No Such Category Found')
        return redirect('Collections')
    
def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug= cate_slug, status=0)):
        if(Product.objects.filter(slug= prod_slug, status=0)):
            products= Product.objects.filter(slug=prod_slug, status=0).first()
            context={'products':products}
        else:
            messages.error(request, 'No such product found')
            return redirect('Collections')
    else:
        messages.error(request, 'No such category found')
        return redirect('Collections')
    return render(request, 'products/view.html', context)

