import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from main.forms import ProductForm
from main.models import Product
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)
    product_count = products.count()

    context = {
        'name': request.user.username,
        'class': 'PBP KKI',
        'products': products,
        'product_count': product_count,
        'plural': 's' if product_count != 1 else '',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, 'main.html', context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, 'create_product.html', context)

@login_required(login_url='/login')
def delete_product(request, id):
    try:
        product = Product.objects.get(pk=id)
        if product.user.id != request.user.id:
            return HttpResponse(status=403)
        product.delete()
        return HttpResponseRedirect(reverse('main:show_main'))
    except Product.DoesNotExist:
        return HttpResponse(status=204)

@login_required(login_url='/login')
def show_products(request):
    products = Product.objects.filter(user=request.user)
    product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
        'plural': 's' if product_count != 1 else '',
    }

    return render(request, 'show_products.html', context)

@login_required(login_url='/login')
def show_xml(request):
    products = Product.objects.filter(user=request.user)
    data = serializers.serialize('xml', products)

    return HttpResponse(data, content_type='application/xml')

@login_required(login_url='/login')
def show_json(request):
    products = Product.objects.filter(user=request.user)
    data = serializers.serialize('json', products)

    return HttpResponse(data, content_type='application/json')

@login_required(login_url='/login')
def show_xml_by_id(request, id):
    print(request.body)
    product = Product.objects.filter(pk=id)
    if product.first().user.id != request.user.id:
        return HttpResponse(status=403)
    data = serializers.serialize('xml', product)

    return HttpResponse(data, content_type='application/xml')

@login_required(login_url='/login')
def show_json_by_id(request, id):
    product = Product.objects.filter(pk=id)
    if product.first().user.id != request.user.id:
        return HttpResponse(status=403)
    data = serializers.serialize('json', product)

    return HttpResponse(data, content_type='application/json')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def increment_amount(request, id):
    product = Product.objects.get(pk=id)
    if request.user.id == product.user.id:
        product.amount += 1
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    else:
        return HttpResponse(status=403)

@login_required(login_url='/login')
def decrement_amount(request, id):
    product = Product.objects.get(pk=id)
    if request.user.id == product.user.id:
        product.amount -= 1
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    else:
        return HttpResponse(status=403)