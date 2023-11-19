import datetime
import json
from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
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
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)
    product_count = products.count()

    if 'last_login' not in request.COOKIES:
        logout(request)

    context = {
        'name': request.user.username,
        'class': 'PBP KKI',
        'products': products,
        'last_login': datetime.datetime.strptime(request.COOKIES['last_login'], '%Y-%m-%d %H:%M:%S.%f'),
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
    
    context = {
        'form': form,
        'last_login': datetime.datetime.strptime(request.COOKIES['last_login'], '%Y-%m-%d %H:%M:%S.%f'),
    }
    return render(request, 'create_product.html', context)

@csrf_exempt
@login_required(login_url='/login')
def create_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        amount = request.POST.get("amount")
        category = request.POST.get("category")
        hidden = request.POST.get("hidden") == "on"
        user = request.user

        try:
            new_product = Product(user=user, name=name, amount=amount, description=description, category=category, price=price, hidden=hidden)
            new_product.save()
        except:
            return HttpResponse(b"Error")

        return HttpResponse(b"OK", status=201)

    return HttpResponse(status=405)

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

@csrf_exempt
@login_required(login_url='/login')
def delete_product_ajax(request):
    if request.method == "POST":
        try:
            product = Product.objects.get(pk=request.POST.get("id"))

            if product.user.id != request.user.id:
                return HttpResponse(status=403)
            product.delete()
            return HttpResponse(b"OK", status=201)
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
        'last_product': products.last(),
    }

    return render(request, 'show_products.html', context)

@login_required(login_url='/login')
def show_xml(request):
    products = Product.objects.filter(user=request.user)
    data = serializers.serialize('xml', products)

    return HttpResponse(data, content_type='application/xml')

@login_required(login_url='/login')
def show_json(request):
    products = Product.objects.filter(user=request.user, hidden=False)
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
        if product.amount != 1:
            product.amount -= 1
            product.save()
        else:
            product.delete()
        return HttpResponseRedirect(reverse('main:show_main'))
    else:
        return HttpResponse(status=403)
    
@csrf_exempt
@login_required(login_url='/login')
def increment_amount_ajax(request):
    if request.method == "POST":
        try:
            product = Product.objects.get(pk=request.POST.get("id"))

            if product.user.id != request.user.id:
                return HttpResponse(status=403)
            product.amount += 1
            product.save()
            return HttpResponse(b"OK", status=201)
        except Product.DoesNotExist:
            return HttpResponse(status=204)

@csrf_exempt
@login_required(login_url='/login')
def decrement_amount_ajax(request):
    if request.method == "POST":
        try:
            product = Product.objects.get(pk=request.POST.get("id"))

            if product.user.id != request.user.id:
                return HttpResponse(status=403)
            product.amount -= 1
            product.save()
            return HttpResponse(b"OK", status=201)
        except Product.DoesNotExist:
            return HttpResponse(status=204)

@login_required(login_url='/login')
def edit_product(request, id):
    # Get product by ID
    product = Product.objects.get(pk=id)
    if request.user.id == product.user.id:
        # Set product as instance of form
        form = ProductForm(request.POST or None, instance=product)

        if form.is_valid() and request.method == "POST":
            # Save the form and return to home page
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))
    else:
        return HttpResponse(status=403)

    context = {'form': form}
    return render(request, "edit_product.html", context)

@csrf_exempt
def create_product_json(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Product.objects.create(
            user = request.user,
            name = data["name"],
            amount = data["amount"],
            description = data["description"],
            category = data["category"],
            price = int(data["price"]),
            hidden = False,
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)