from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.urls import reverse
from main.forms import ProductForm
from main.models import Product

# Create your views here.
def show_main(request):
    products = Product.objects.all()
    product_count = products.count()

    context = {
        'name': 'Muhammad Oka',
        'class': 'PBP KKI',
        'products': products,
        'product_count': product_count,
        'plural': 's' if product_count != 1 else '',
    }

    return render(request, 'main.html', context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, 'create_product.html', context)

def delete_product(request, id):
    try:
        product = Product.objects.get(pk=id)
        product.delete()
        return HttpResponseRedirect(reverse('main:show_main'))
    except Product.DoesNotExist:
        return HttpResponse(status=204)

def show_products(request):
    products = Product.objects.all()
    product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
        'plural': 's' if product_count != 1 else '',
    }

    return render(request, 'show_products.html', context)

def show_xml(request):
    products = Product.objects.all()
    data = serializers.serialize('xml', products)

    return HttpResponse(data, content_type='application/xml')

def show_json(request):
    products = Product.objects.all()
    data = serializers.serialize('json', products)

    return HttpResponse(data, content_type='application/json')

def show_xml_by_id(request, id):
    product = Product.objects.filter(pk=id)
    data = serializers.serialize('xml', product)

    return HttpResponse(data, content_type='application/xml')

def show_json_by_id(request, id):
    product = Product.objects.filter(pk=id)
    data = serializers.serialize('json', product)

    return HttpResponse(data, content_type='application/json')