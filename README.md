# [Inventaris](https://oka-inventaris.adaptable.app/)
#### Muhammad Oka - 2206046784

## Assignment Steps
### Assignment 2
<details>
<summary>Create a new Django project</summary>

1. Create new directory and initialize a virtual environment

    ```bash
    mkdir inventaris && cd inventaris
    python3 -m venv env
    ```
2. Activate the virtual environment

    ```bash
    source env/bin/activate
    ```

3. Create requirements.txt

    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```

4. Install requirements

    ```bash
    pip install -r requirements.txt
    ```

5. Create new Django project
    
    ```bash
    django-admin startproject inventaris .
    ```

6. Set ```ALLOWED_HOST``` to any host in ```settings.py```

    ```python
    # inventaris/settings.py

    ALLOWED_HOSTS = ['*']
    ```
</details>

<details>
<summary>Create an app with the name main on that project</summary>

1. Create an app with the name ```main```

    ```bash
    python manage.py startapp main
    ```
2. Add ```main``` to ```INSTALLED_APPS``` in ```settings.py```

    ```python
    # inventaris/settings.py

    INSTALLED_APPS = [
        'main',
    ]
    ```

</details>

<details>
<summary>Create a URL routing configuration to acces the main app</summary>

1. Add URL routing to ```urls.py```

    ```python
    # inventaris/urls.py

    urlpatterns = [
        path('', include('main.urls')),
    ]

    ```
    
</details>

<details>
<summary>Create a model on the main app with the name Item</summary>

1. Create a model with name ```Item``` in ```models.py```

    ```python
    # main/views.py

    from django.db import models

    # Create your models here.
    class Item(models.Model):
        name = models.CharField(max_length=100)
        amount = models.IntegerField()
        description = models.TextField()
        category = models.CharField(max_length=100)
        price = models.IntegerField()
    ```
    
</details>

<details>
<summary>Create a function in views.py that returns an HTML template containing your application name, your name, and your class</summary>

1. Create the templates folder in ```main/```

    ```bash
    cd main
    mkdir templates
    ```
    
2. Create the HTML template file for the main app

    ```html
    <!-- main/templates/main.html -->
    <h1>Inventaris</h1>

    <h5>Name: </h5>
    <p>{{ name }}</p>
    <h5>Class: </h5>
    <p>{{ class }}</p>
    ```

3. Create the view function for the main app in ```views.py```

    ```python
    # main/views.py

    from django.shortcuts import render

    # Create your views here.
    def show_main(request):
        context = {
            'name': 'Muhammad Oka',
            'class': 'PBP KKI',
        }

        return render(request, 'main.html', context)
    ```

</details>

<details>
<summary>Create a routing in urls.py to map the function in views.py to a URL</summary>

1. Create the routing in ```urls.py```

    ```python
    # main/urls.py

    from django.urls import path
    from main.views import show_main

    app_name = 'main'
    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
    
</details>

<details>
<summary>Create basic tests</summary>

1. Create new tests in ```tests.py```

    ```python
    # main/tests.py

    from django.test import TestCase, Client
    from django.http import HttpResponse

    # Create your tests here.
    class MainTest(TestCase):
        def test_main_exists(self):
            response: HttpResponse = Client().get('/')
            self.assertEquals(response.status_code, 200)
        
        def test_main_template_test(self):
            response: HttpResponse = Client().get('/')
            self.assertTemplateUsed(response, 'main.html')

        def test_main_information_test(self):
            response: HttpResponse = Client().get('/')
            self.assertContains(response, "Muhammad Oka")
            self.assertContains(response, "PBP KKI")
    ```
    
</details>

### Assignment 3
<details>
<summary>Create a form input to add a model object to the previous app.</summary>

1. Create ```forms.py``` in the main subdirectory

    ```python
    # main/forms.py

    from django.forms import ModelForm
    from main.models import Product

    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ['name', 'amount', 'description', 'category', 'price']
    ```
2. Create a base template

    ```html
    <!-- templates/base.html -->

    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta
                name="viewport"
                content="width=device-width, initial-scale=1.0"
            />
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500;700;900&display=swap" rel="stylesheet">
            {% block meta %}
            {% endblock meta %}
        </head>

        <body style="display: flex; align-items: center; flex-direction: column; font-family: 'Roboto', sans-serif;">
            {% block content %}
            {% endblock content %}
        </body>
    </html>
    
    ```
3. Add root templates folder to ```settings.py```

    ```python
    # inventaris/settings.py

    # ...
    TEMPLATES = [
        {
            # ...
            'DIRS': [BASE_DIR / 'templates'],
            # ...
        },
    ]
    # ...
    ```

4. Create new template ```product_table.html```

    ```html
    <!-- main/templates/product_table.html -->
    
    {% block content %}
    <table style="text-align: center; border: 1px solid; border-collapse: collapse;">
        <tr>
            <th style="padding-top: 0.25em; padding-bottom: 0.25em; padding-left: 2em; padding-right: 2em; border: 1px solid; border-collapse: collapse;">Name</th>
            <th style="padding-top: 0.25em; padding-bottom: 0.25em; padding-left: 2em; padding-right: 2em; border: 1px solid; border-collapse: collapse;">Amount</th>
            <th style="padding-top: 0.25em; padding-bottom: 0.25em; padding-left: 2em; padding-right: 2em; border: 1px solid; border-collapse: collapse;">Description</th>
            <th style="padding-top: 0.25em; padding-bottom: 0.25em; padding-left: 2em; padding-right: 2em; border: 1px solid; border-collapse: collapse;">Category</th>
            <th style="padding-top: 0.25em; padding-bottom: 0.25em; padding-left: 2em; padding-right: 2em; border: 1px solid; border-collapse: collapse;">Price</th>
            <th style="padding-top: 0.25em; padding-bottom: 0.25em; padding-left: 2em; padding-right: 2em; border: 1px solid; border-collapse: collapse;">Date Added</th>
        </tr>

        {% comment %} Below is how to show the product data {% endcomment %}

        {% for product in products %}
            <tr>
                <td style="padding-top: 0.25em; padding-bottom: 0.25em; padding-left: 2em; padding-right: 2em; border: 1px solid; border-collapse: collapse;">{{product.name}}</td>
                <td style="padding-top: 0.25em; padding-bottom: 0.25em; padding-left: 2em; padding-right: 2em; border: 1px solid; border-collapse: collapse;">{{product.amount}}</td>
                <td style="padding-top: 0.25em; padding-bottom: 0.25em; padding-left: 2em; padding-right: 2em; border: 1px solid; border-collapse: collapse;">{{product.description}}</td>
                <td style="padding-top: 0.25em; padding-bottom: 0.25em; padding-left: 2em; padding-right: 2em; border: 1px solid; border-collapse: collapse;">{{product.category}}</td>
                <td style="padding-top: 0.25em; padding-bottom: 0.25em; padding-left: 2em; padding-right: 2em; border: 1px solid; border-collapse: collapse;">{{product.price}}</td>
                <td style="padding-top: 0.25em; padding-bottom: 0.25em; padding-left: 2em; padding-right: 2em; border: 1px solid; border-collapse: collapse;">{{product.date_added}}</td>
                <td style="padding-top: 0.25em; padding-bottom: 0.25em; padding-left: 1em; padding-right: 1em; border: 1px solid; border-collapse: collapse;">
                    <a href="/products/delete/{{product.id}}">
                        <button>X</button>
                    </a>
                </td>
            </tr>
        {% endfor %}
    </table>

    <h5>Total: {{product_count}} product{{plural}}</h5>
    {% endblock content %}
    ```

5. Update the ```main.html``` template
    ```html
    <!-- main/templates/main.html -->

    {% extends 'base.html' %}

    {% block content %}
    <h1 style="font-weight: 900; font-size: 3em;">INVENTARIS</h1>
    <div style="display: flex; gap: 1em;">
        <h3>Name: {{name}}</h3>
        <h3>Class: {{class}}</h3>
    </div>

    {% include 'product_table.html' %}

    <a href="{% url 'main:create_product' %}">
        <button>
            Add New Product
        </button>
    </a>
    {% endblock content %}
    
    ```

6. Create a new template ```create_product.html``` and make the form to POST data

    ```html
    <!-- main/templates/create_product.html -->

    {% extends 'base.html' %}

    {% block content %}
    <h1>Add New Product</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Product"/>
                </td>
            </tr>
        </table>
    </form>
    {% endblock content %}
    ```

7. Create the view to create product

    ```python
    # main/views.py

    # ...
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == 'POST':
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))
        
        context = {'form': form}
        return render(request, 'create_product.html', context)
    # ...
    ```
    
8. Create the url routing to create product

    ```py
    # main/urls.py

    # ...
    urlpatterns = [
        # ...
        path('products/create/', create_product, name='create_product'),
        # ...
    ]
    # ...
    ```

</details>

<details>
<summary>Add 5 views to view the added objects in HTML, XML, JSON, XML by ID, and JSON by ID formats.</summary>

1. Create new template ```show_products.html``` to show the products in HTML.

    ```html
    <!-- main/templates/show_products.html -->
    
    {% extends 'base.html' %}

    {% block content %}
    <h1>Products List</h1>

    {% include 'product_table.html' %}
    {% endblock content %}
    ```

2. Add new views to ```views.py```

    ```python
    # main/views.py

    # ...
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
    ```
    
</details>

<details>
<summary>Create URL routing for each of the views added in point 2.</summary>

1. Add new routings to ```urls.py```

    ```python
    # main/urls.py

    # ...
    urlpatterns = [
        path('', show_main, name='show_main'),
        path('products/', show_products, name='show_products'),
        path('products/create/', create_product, name='create_product'),
        path('products/delete/<int:id>/', delete_product, name='delete_product'),
        path('products/xml/', show_xml, name='show_xml'),
        path('products/xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('products/json/', show_json, name='show_json'),
        path('products/json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    ]
    ```

</details>

### Assignment 4

<details>

<summary>Implement registration, login, and logout functions</summary>

1. Create the ```register.html``` template

    ```html
    <!-- main/templates/register.html -->

    {% extends 'base.html' %}

    {% block meta %}
        <title>Register</title>
    {% endblock meta %}

    {% block content %}  
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}
    {% endblock content %}
    ```
2. Add new view for the register form

    ```py
    # main/views.py

    # ...
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
    # ...
    ```

3. Create the ```login.html``` template

    ```html
    <!-- main/templates/login.html -->

    {% extends 'base.html' %}

    {% block meta %}
        <title>Login</title>
    {% endblock meta %}

    {% block content %}

    <h1 style="font-weight: 900; font-size: 3em;">INVENTARIS</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

    {% endblock content %}
    ```
4. Create a new view for the login form

    ```py
    # main/views.py

    # ...
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
    # ...
    ```

5. Create the view to handle logging out

    ```py
    # main/views.py

    # ...
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    # ...
    ```

6. Route the created views

    ```py
    # main/urls.py

    urlpatterns = [
        # ...
        path('register/', register, name='register'),
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
        # ...
    ]
    ```

</details>

<details>

<summary>Create two user accounts with three dummy data entries for each account</summary>

### First user

![User1](https://cdn.discordapp.com/attachments/1057322303731548192/1156282140854603807/image.png?ex=65146729&is=651315a9&hm=11e75d2890d91dea2dca596b92351094b036b9db12d49fd932dfcb3d4e6f5782&)

### Second user

![User2](https://cdn.discordapp.com/attachments/1057322303731548192/1156282688626503690/image.png?ex=651467ab&is=6513162b&hm=f7913c63808a2791df28f49725ef2f0d85a3e24cf3b948a69f2083c0b5c71c83&)

</details>

<details>

<summary>Connect Item model with User</summary>

1. Add user field to model

    ```py
    # main/models.py

    class Product(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        # ...
    ```
2. Modify the ```create_product``` view to add the user to the product entity

    ```py
    # main/views.py

    # ...
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == 'POST':
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return HttpResponseRedirect(reverse('main:show_main'))
        
        context = {'form': form}
        return render(request, 'create_product.html', context)
    # ...
    ```
3. Change the context of the ```show_main``` view to display the username

    ```py
    context = {
        'name': request.user.username,
        # ...
    }
    ```

</details>

<details>

<summary>Display the information of the logged-in user and applying cookies</summary>

1. Add a ```last_login``` cookie when user logs in

    ```py
    # main/views.py

    # ...
    def login_user(request):
        if request.method == 'POST':
            # ...
            if user is not None:
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main")) 
                response.set_cookie('last_login', str(datetime.datetime.now()))
            # ...
    # ...
    ```

2. Add the ```last_login``` cookie to the ```show_main``` context

    ```py
    # main/views.py

    # ...
    context = {
        # ...
        'last_login': request.COOKIES['last_login'],
        # ...
    }
    # ...
    ```

3. Add the ```last_login``` to the HTML template

    ```html
    <!-- main/templates/main.html -->
    
    <!-- ... -->
    <h5>Last login session: {{ last_login }}</h5>
    <!-- ... -->
    ```

</details>

<details>

<summary>Implementing authorization</summary>

1. Add ```@login_required(login_url='/login')``` to views that needs a login

    ```py
    # main/views.py

    @login_required(login_url='/login')
        def show_main(request):

    @login_required(login_url='/login')
        def create_product(request):

    @login_required(login_url='/login')
        def delete_product(request, id):

    @login_required(login_url='/login')
        def show_products(request):

    @login_required(login_url='/login')
        def show_xml(request):

    @login_required(login_url='/login')
        def show_json(request):
    
    @login_required(login_url='/login')
        def show_xml_by_id(request, id):
    
    @login_required(login_url='/login')
        def show_json_by_id(request, id):
    
    ```

2. Add checks to make sure user is modifying and showing their own products

    ```py
    @login_required(login_url='/login')
    def delete_product(request, id):
        try:
            product = Product.objects.get(pk=id)
            if product.user.id != request.user.id:
                return HttpResponse(status=403)
            # ...
        # ...
    
    @login_required(login_url='/login')
    def show_products(request):
        products = Product.objects.filter(user=request.user)
        # ...
    
    @login_required(login_url='/login')
    def show_xml(request):
        products = Product.objects.filter(user=request.user)
        # ...
    
    @login_required(login_url='/login')
    def show_json(request):
        products = Product.objects.filter(user=request.user)
        # ...
    
    @login_required(login_url='/login')
    def show_xml_by_id(request, id):
        product = Product.objects.filter(pk=id)
        if product.first().user.id != request.user.id:
            return HttpResponse(status=403)
        # ...
    
    @login_required(login_url='/login')
    def show_json_by_id(request, id):
        product = Product.objects.filter(pk=id)
        if product.first().user.id != request.user.id:
                return HttpResponse(status=403)
        # ...
    ```

</details>

<details>

<summary>Add a button to increment the amount of an item and a button to decrement the amount of an item</summary>

1. Create the views to increment and decrement the amount of an item

    ```py
    # main/views.py

    # ...
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
    ```

2. Add the buttons to the HTML template

    ```html
    <!-- main/templates/product_table.html -->

    <!-- ... -->
    <td style="padding-top: 0.25em; padding-bottom: 0.25em; padding-left: 2em; padding-right: 2em; border: 1px solid; border-collapse: collapse;">
        <div style="display: flex; justify-content: center; gap: 10px;">
            <form method="post" action="/products/decrement/{{product.id}}/">
                {% csrf_token %}
                <button>-</button>
            </form>
            {{product.amount}}
            <form method="post" action="/products/increment/{{product.id}}/">
                {% csrf_token %}
                <button>+</button>
            </form>
        </div>
    </td>
    <!-- ... -->
    ```

3. Route the create views

    ```py
    # main/urls.py

    urlpatterns = [
        # ...
        path('products/increment/<int:id>/', increment_amount, name='increment_amount'),
        path('products/decrement/<int:id>/', decrement_amount, name='decrement_amount'),
        # ...
    ]
    
    ```

</details>

<details>

<summary>Add a button to delete an item from the inventory</summary>

1. Create the view to delete an item

    ```py
    # main/views.py
    
    # ...
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
    # ...
    ```

2. Add the delete button in the HTML template

    ```html
    <!-- main/templates/product_table.html -->
    <!-- ... -->
    <td style="padding-top: 0.25em; padding-bottom: 0.25em; padding-left: 1em; padding-right: 1em; border: 1px solid; border-collapse: collapse;">
        <form method="post" action="/products/delete/{{product.id}}/">
            {% csrf_token %}
            <button>X</button>
        </form>
    </td>
    <!-- ... -->
    ```

3. Route the created view

    ```py
    # main/urls.py

    urlpatterns = [
        # ...
        path('products/delete/<int:id>/', delete_product, name='delete_product'),
        # ...
    ]
    
    ```

</details>

### Assignment 5

<details>

<summary>Install Tailwind</summary>

1. Install django-tailwind package

    ```bash
    pip install django-tailwind
    ```

2. Add tailwind to INSTALLED_APPS

    ```py
    # inventaris/settings.py

    INSTALLED_APPS = [
        # ...
        'tailwind',
    ]
    ```

3. Initialize tailwind app

    ```bash
    python manage.py tailwind init
    ```

4. Add the created app to INSTALLED_APPS

    ```py
    # inventaris/settings.py

    INSTALLED_APPS = [
        # ...
        'tailwind',
        'theme',
    ]
    ```

5. Add new variables for tailwind in settings.py

    ```py
    # inventaris/settings.py

    TAILWIND_APP_NAME = 'theme'
    INTERNAL_IPS = [
        "127.0.0.1",
    ]
    
    ```

7. Install tailwind

    ```bash
    python manage.py tailwind install
    ```

8. Add tailwind to the base template

    ```html
    <!-- templates/base.html -->

    {% load static %}
    {% load static tailwind_tags %}
    <html>
        <head>
            <!-- ... -->
            {% tailwind_css %}
            <!-- ... -->
        </head>
        <!-- ... -->
    </html>

    ```

9. Start tailwind

    ```bash
    python manage.py tailwind start
    ```

</details>

<details>

<summary>Modify templates to use Tailwind</summary>

1. Create a new navbar

    ```html
    <!-- main/templates/navbar.html -->

    {% block content %}
    <div class="min-w-full flex justify-between px-8 py-4 bg-cyan-500">
        <div class="flex items-center gap-4">
            <a href="/" class="text-4xl font-black">INVENTARIS</a>
            <a href="{% url 'main:create_product' %}" class="text-4xl hover:text-green-400 transition-colors">
                <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-plus-circle" viewBox="0 0 16 16">
                    <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
                    <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>
                </svg>
            </a>
        </div>
        <div class="flex flex-col items-end text-right">
            <p class="text-2xl leading-snug">Welcome, <span class="font-bold">{{ user.username }}</span> (PBP KKI)</p>
            <p class="text-lg leading-snug">Last login: {{ last_login }}</p>
            <a href="{% url 'main:logout' %}" class=" hover:text-red-500 hover:font-semibold transition-all w-max leading-snug">Logout</a>
        </div>
    </div>
    {% endblock %}
    ```

2. Modify product_table template

    ```html
    <!-- main/templates/product_table.html -->
    
    {% block content %}
    <div class="flex flex-col justify-center items-center gap-6">
        <table>
            <tr class="bg-neutral-500 border border-neutral-300 text-center">
                <th class="px-12 py-2">Name</th>
                <th class="px-12 py-2">Amount</th>
                <th class="px-12 py-2">Description</th>
                <th class="px-12 py-2">Category</th>
                <th class="px-12 py-2">Price</th>
                <th class="px-12 py-2">Date Added</th>
                <th></th>
            </tr>
            {% for product in products %}
            <tr class="border border-neutral-300 {% if product == last_product %} bg-cyan-700 {% else %} bg-neutral-700 {% endif %} text-white text-center">
                <td class="px-12 py-2">{{product.name}}</td>
                <td class="px-12 py-2">
                    <div class="flex justify-center items-center gap-4">
                        <form method="post" action="/products/decrement/{{product.id}}/">
                            {% csrf_token %}
                            <button class="p-[2px] text-lg hover:text-green-400 transition-colors">-</button>
                        </form>
                        {{product.amount}}
                        <form method="post" action="/products/increment/{{product.id}}/">
                            {% csrf_token %}
                            <button class="p-[2px] text-lg hover:text-green-400 transition-colors">+</button>
                        </form>
                    </div>
                </td>
                <td class="px-12 py-2">{{product.description}}</td>
                <td class="px-12 py-2">{{product.category}}</td>
                <td class="px-12 py-2">{{product.price}}</td>
                <td class="px-12 py-2">{{product.date_added}}</td>
                <td class="px-12 py-2">
                    <div class="flex gap-2">
                        <form method="post" action="/products/edit/{{product.id}}/" class="flex justify-center items-center">
                            {% csrf_token %}
                            <button class="hover:text-green-400 transition-colors">
                                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
                                    <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                                    <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
                                </svg>
                            </button>
                        </form>
                        <form method="post" action="/products/delete/{{product.id}}/" class="flex justify-center items-center">
                            {% csrf_token %}
                            <button class="hover:text-red-500 transition-colors">
                                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-trash3-fill" viewBox="0 0 16 16">
                                    <path d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5Zm-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5ZM4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998.06Zm6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47-.528ZM8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5Z"/>
                                </svg>
                            </button>
                        </form>
                    </div>
                </td>
            </tr>
            {% endfor %}
        </table>
        <p>Total products: {{product_count}} product{{plural}}</p>
    </div>
    {% endblock content %}
    ```

3. Modify the login template

    ```html
    <!-- main/templates/login.html -->
    
    {% extends 'base.html' %}

    {% block content %}
    <div class="h-screen grid grid-cols-2 justify-center items-center">
        <div class="min-h-screen flex justify-end items-center p-16 bg-cyan-500">
            <h1 class="font-black text-white text-5xl">INVENTARIS</h1>
        </div>
        <div class="min-h-screen flex justify-center items-start flex-col p-16 gap-8">
            <form method="POST" action="/login/">
                {% csrf_token %}
                <div class="flex flex-col gap-4 items-center">
                    <div class="grid grid-row-2 gap-4">
                        <div class="flex justify-center items-center gap-4">
                            <label for="username" class="text-xl">Username:</label>
                            <input type="text" name="username" placeholder="Username" required class="form-control text-black appearance-none outline-none border-none rounded focus:shadow-none focus:border-none focus:ring-0 hover:outline-cyan-500 hover:outline-2 focus:outline-cyan-500 focus:outline-2 transition-[outline]">
                        </div>
                        <div class="flex justify-center items-center gap-4">
                            <label for="password" class="text-xl">Password:</label>
                            <input type="password" name="password" placeholder="Password" required class="form-control text-black appearance-none outline-none border-none rounded focus:shadow-none focus:border-none focus:ring-0 hover:outline-cyan-500 hover:outline-2 focus:outline-cyan-500 focus:outline-2 transition-[outline]">
                        </div>
                    </div>
                    <input class="border-2 border-cyan-500 bg-cyan-800 hover:bg-cyan-500 text-white px-3 py-1 rounded hover:cursor-pointer transition-colors" type="submit" value="Login">
                </div>
            </form>
        
            {% if messages %}
                <ul>
                    {% for message in messages %}
                        {% if message.tags == 'success' %}
                            <li class="text-green-500 font-semibold text-lg">{{ message }}</li>
                        {% else %}
                            <li class="text-red-500 font-semibold text-lg">{{ message }}</li>
                        {% endif %}
                    {% endfor %}
                </ul>
            {% endif %}     
                
            <p class="text-lg">Don't have an account yet? <a href="{% url 'main:register' %}" class="hover:text-cyan-500 transition-colors">Register Now</a></p>
        </div>
    </div>
    {% endblock content %}
    ```

4. Modify the register template

    ```html
    <!-- main/templates/register.html -->
    
    {% extends 'base.html' %}

    {% block content %}  
    <div class="h-screen grid grid-cols-2 justify-center items-center">
        <div class="min-h-screen flex justify-end items-center p-16 gap-4 bg-cyan-500">
            <a href="/">
                <svg xmlns="http://www.w3.org/2000/svg" width="38" height="38" fill="currentColor" class="bi bi-chevron-left" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M11.354 1.646a.5.5 0 0 1 0 .708L5.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0z"/>
                </svg>
            </a>
            <h1 class="font-black text-white text-5xl">INVENTARIS</h1>
        </div>
        <div class="min-h-screen flex justify-center items-start flex-col p-16 gap-8">
            <p class="text-2xl font-semibold">Register New User</p>
            <form method="POST" action="/register/">
                {% csrf_token %}
                <div class="flex flex-col gap-4">
                    <div class="grid grid-row-2 gap-4">
                        <div class="flex justify-between items-center gap-4">
                            <label for="username" class="text-xl">Username:</label>
                            <input type="text" name="username" placeholder="Username" maxlength="150" autocapitalize="none" required class="form-control text-black appearance-none outline-none border-none rounded focus:shadow-none focus:border-none focus:ring-0 hover:outline-cyan-500 hover:outline-2 focus:outline-cyan-500 focus:outline-2 transition-[outline]">
                        </div>
                        <div class="flex justify-between items-center gap-4">
                            <label for="password" class="text-xl">Password:</label>
                            <input type="password" name="password1" placeholder="Password" required class="form-control text-black appearance-none outline-none border-none rounded focus:shadow-none focus:border-none focus:ring-0 hover:outline-cyan-500 hover:outline-2 focus:outline-cyan-500 focus:outline-2 transition-[outline]">
                        </div>
                        <div class="flex justify-between items-center gap-4">
                            <label for="password" class="text-xl">Password Confirmation:</label>
                            <input type="password" name="password2" placeholder="Password Confirmation" required class="form-control text-black appearance-none outline-none border-none rounded focus:shadow-none focus:border-none focus:ring-0 hover:outline-cyan-500 hover:outline-2 focus:outline-cyan-500 focus:outline-2 transition-[outline]">
                        </div>
                    </div>
                    <input class="border-2 border-cyan-500 bg-cyan-800 hover:bg-cyan-500 text-white px-3 py-1 rounded hover:cursor-pointer transition-colors" type="submit" value="Register">
                </div>
            </form>
        
            {% if messages %}
                <ul>
                    {% for message in messages %}
                        <li class="text-red-500 font-semibold text-lg">{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}     
            {% if form.errors.username %}
                <ul>
                    <li class="text-red-500 font-semibold text-lg">{{ form.errors.username }}</li>
                </ul>
            {% endif %}        
            {% if form.errors.password1 %}
                <ul>
                    <li class="text-red-500 font-semibold text-lg">{{ form.errors.password1 }}</li>
                </ul>
            {% endif %}        
            {% if form.errors.password2 %}
                <ul>
                    <li class="text-red-500 font-semibold text-lg">{{ form.errors.password2 }}</li>
                </ul>
            {% endif %}        
        </div>
    </div>
    {% endblock content %}
    ```

5. Modify the create_product template

    ```html
    <!-- main/templates/create_product.html -->
    
    {% extends 'base.html' %} 

    {% block content %}
    {% include 'navbar.html' %}
    <div class="flex flex-col justify-center items-center gap-8 p-8">
        <h1 class="text-2xl font-semibold">Create New Product</h1>
        <form method="POST" class="w-max flex flex-col gap-8">
            {% csrf_token %}
            <div class="grid grid-cols-2 gap-4 items-center">
                <label for="id_name">Name:</label>
                <input type="text" name="name" maxlength="100" required id="id_name" class="form-control text-black appearance-none outline-none border-none rounded focus:shadow-none focus:border-none focus:ring-0 hover:outline-cyan-500 hover:outline-2 focus:outline-cyan-500 focus:outline-2 transition-[outline]">
                <label for="id_amount">Amount:</label>
                <input type="text" name="amount" required id="id_amount" class="form-control text-black appearance-none outline-none border-none rounded focus:shadow-none focus:border-none focus:ring-0 hover:outline-cyan-500 hover:outline-2 focus:outline-cyan-500 focus:outline-2 transition-[outline]">
                <label for="id_amount">Description:</label>
                <textarea name="description" cols="40" rows="10" required id="id_description" class="form-control text-black appearance-none outline-none border-none rounded focus:shadow-none focus:border-none focus:ring-0 hover:outline-cyan-500 hover:outline-2 focus:outline-cyan-500 focus:outline-2 transition-[outline]"></textarea>
                <label for="id_category">Category:</label>
                <input type="text" name="category" maxlength="100" required id="id_category" class="form-control text-black appearance-none outline-none border-none rounded focus:shadow-none focus:border-none focus:ring-0 hover:outline-cyan-500 hover:outline-2 focus:outline-cyan-500 focus:outline-2 transition-[outline]">
                <label for="id_price">Price:</label>
                <input type="text" name="price" required id="id_price" class="form-control text-black appearance-none outline-none border-none rounded focus:shadow-none focus:border-none focus:ring-0 hover:outline-cyan-500 hover:outline-2 focus:outline-cyan-500 focus:outline-2 transition-[outline]">
            </div>
            <input class="border-2 border-cyan-500 bg-cyan-800 hover:bg-cyan-500 text-white px-3 py-1 rounded hover:cursor-pointer transition-colors" type="submit" value="Create">
        </form>
    </div>
    {% endblock content %}
    ```

</details>

<details>

<summary>Create edit function</summary>

1. Create the view to edit products

    ```py
    # main/views.py

    # ...
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
    # ...
    ```

2. Create a template for the view

    ```html
    <!-- main/templates/edit_product.html -->
    
    {% extends 'base.html' %} 

    {% block content %}
    {% include 'navbar.html' %}
    <div class="flex flex-col justify-center items-center gap-8 p-8">
        <h1 class="text-2xl font-semibold">Edit Product</h1>
        <form method="POST" class="w-max flex flex-col gap-8">
            {% csrf_token %}
            <div class="grid grid-cols-2 gap-4 items-center">
                <label for="id_name">Name:</label>
                <input type="text" name="name" maxlength="100" required id="id_name" class="form-control text-black appearance-none outline-none border-none rounded focus:shadow-none focus:border-none focus:ring-0 hover:outline-cyan-500 hover:outline-2 focus:outline-cyan-500 focus:outline-2 transition-[outline]" value="{{form.instance.name}}"></input>
                <label for="id_amount">Amount:</label>
                <input type="text" name="amount" required id="id_amount" class="form-control text-black appearance-none outline-none border-none rounded focus:shadow-none focus:border-none focus:ring-0 hover:outline-cyan-500 hover:outline-2 focus:outline-cyan-500 focus:outline-2 transition-[outline]"  value="{{form.instance.amount}}">
                <label for="id_amount">Description:</label>
                <textarea name="description" cols="40" rows="10" required id="id_description" class="form-control text-black appearance-none outline-none border-none rounded focus:shadow-none focus:border-none focus:ring-0 hover:outline-cyan-500 hover:outline-2 focus:outline-cyan-500 focus:outline-2 transition-[outline]">{{form.instance.description}}</textarea>
                <label for="id_category">Category:</label>
                <input type="text" name="category" maxlength="100" required id="id_category" class="form-control text-black appearance-none outline-none border-none rounded focus:shadow-none focus:border-none focus:ring-0 hover:outline-cyan-500 hover:outline-2 focus:outline-cyan-500 focus:outline-2 transition-[outline]" value="{{form.instance.category}}">
                <label for="id_price">Price:</label>
                <input type="text" name="price" required id="id_price" class="form-control text-black appearance-none outline-none border-none rounded focus:shadow-none focus:border-none focus:ring-0 hover:outline-cyan-500 hover:outline-2 focus:outline-cyan-500 focus:outline-2 transition-[outline]" value="{{form.instance.price}}">
            </div>
            <input class="border-2 border-cyan-500 bg-cyan-800 hover:bg-cyan-500 text-white px-3 py-1 rounded hover:cursor-pointer transition-colors" type="submit" value="Edit">
        </form>
    </div>
    {% endblock content %}
    ```

3. Add routings for the edit_product view

    ```py
    # main/urls.py

    urlpatterns = [
        # ...
        path('products/edit/<int:id>/', edit_product, name='edit_product'),
        # ...
    ]
    ```

4. Add the edit button on the product_table template

    ```html
    <!-- main/templates/product_table.html -->

    <form method="post" action="/products/edit/{{product.id}}/" class="flex justify-center items-center">
        {% csrf_token %}
        <button class="hover:text-green-400 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
                <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
            </svg>
        </button>
    </form>
    ```

</details>

<details>

<summary>Add functionality to highlight the last product</summary>

1. Add last_product context to show_main view

    ```py
    # main/views.py

    # ...
    @login_required(login_url='/login')
    def show_main(request):
        # ...
        context = {
            # ...
            'last_product': products.last(),
            # ...
        }
    # ...
    ```

2. Add if condition on the class of the table row

    ```html
    <!-- main/templates/product_table.html -->
    
    <!-- ... -->
    {% for product in products %}
        <tr class="border border-neutral-300 {% if product == last_product %} bg-cyan-700 {% else %} bg-neutral-700 {% endif %} text-white text-center">
            <!-- ... -->
        <!-- ... -->
    <!-- ... -->
    ```

</details>

## Assignment Essay

<details>

<summary>Assignment 2</summary>

## Django Web App Diagram
![Django Diagram](https://cdn.discordapp.com/attachments/1057322303731548192/1150633658449924136/django.png)

When the user is accessing a Django-based website, the ```urls.py``` will try to recognize which section of the website the user is trying to access. For example, if the user is accessing ```localhost:8000/login```, then ```urls.py``` will try to find if there is a routing for ```login/```.


If there is a ```login/``` in ```urls.py```, then it will access the views associated to the url in the ```views.py``` file.

The ```views.py``` file will return the HTML template and will be rendered to the user.

The ```views.py``` could communicate with ```models.py``` if data is needed.

And ```models.py``` will comunicate with the Database to get and post the data.

## The Purpose of Virtual Environment

The purpose of virtual environments are to help isolate the Python version and the packages used in different projects. It is possible to create a Django project without one, but it would be easier and more 'correct' to use a virtual environment. The reason why virtual environment is used so that packages between projects are not conflicting. You could have the case where one project have a lower version of a package than the other project. On that case, using a virtual environment will make it easier to manage Python and package version between different projects.

## MVC, MVT, MVVM

**MVC** stands for **Model-View-Controller**. The model stores data and the application logic. The view display the data, and the Controller acts as the middle-man between the model and the view.

**MVT** stands for **Model-View-Template**. The model and View are the same with MVC. But the big difference between MVT and MVC is, MVT use a template to define the user interface.

**MVVM** stands for **Model-View-ViewModel**. The model and view are the same as the other two. The ViewModel acts as a 'converter' to convert the models to a view that can be rendered to the user.

</details>

<details>

<summary>Assignment 3</summary>

## POST vs GET

Forms using the POST method is intended to send the data from the form to the server. Forms using the GET method is inteded to get data from the server and not change anything on the server.

## HTML, JSON, XML

HTML is used to describe how a data is displayed. JSON and XML are used as a way to store data. The difference between JSON and XML is, JSON uses key-value pairs, whereas XML uses a tree.

## Why is JSON commonly used in Web Development

JSON is more common because it's more human-readable and more simple than XML. JSON is also easier to parse for programming languages. It can be converted into a dictionary in Python and object in JS.

## Check API Endpoint with Postman

### GET /products
![GET /products](https://cdn.discordapp.com/attachments/1057322303731548192/1152510286750830622/image.png)

### GET /products/xml
![GET /products/xml](https://cdn.discordapp.com/attachments/1057322303731548192/1152510344372178944/image.png)

### GET /products/xml/5
![GET /products/xml/5](https://cdn.discordapp.com/attachments/1057322303731548192/1152510476538888323/image.png)

### GET /products/json
![GET /products/json](https://cdn.discordapp.com/attachments/1057322303731548192/1152510409253867520/image.png)

### GET /products/json/5
![GET /products/json/5](https://cdn.discordapp.com/attachments/1057322303731548192/1152510530016268318/image.png)

</details>

<details>

<summary>Assignment 4</summary>

## UserCreationForm

```UserCreationForm``` is one of the built-in forms in Django that aids in creating users. It has many features, including password strength, password confirmation, checking if password is similiar to the username, and other.

The main advantage of ```UserCreationForm``` is it is plug and play, you just import the form and you can use them immediately. And one other advantage is you don't need to implement the security features. But one of the disadvantages are the form itself is not very customizable.

## Authentication vs Authorization

Authentication is an act of proving if someone is who they are. Authorization is an act of proving if someone has access to something. Both is needed in an application. Because if we don't have authentication, our authorization is useless because anyone can be any user. If we don't have authorization, someone can access something that they should not have access to.
## Cookies

Cookies are datas that is generated by a website that is stored in the client's browser. Cookies are most commonly used to identify a user. Django uses a session id to identify a user that is accessing the website.

Cookies itself is secure. But if not used correctly, it can pose security issues. Actors could impersonate a user or collect sensitive data from the user.
</details>

<details>

<summary>Assignment 5</summary>

### CSS Element Selector

The ```.``` selector is used for selecting classes. The ```#``` selector is used to select id. You can also select any HTML tags (e.g. ```p``` or ```h1```). You can group elements that needs the same CSS (e.g. ```p, h1, h2```). You can select all elements using the ```*``` selector.

### HTML5 Tags

1. ```<audio>```: To embed an audio file
2. ```<nav>```: Represents a navigation bar/links
3. ```<main>```: Represents the main or dominant section of a document

### Margin vs Padding

Margin defines the amount of space outside of the element, padding defines the amount of space surrounding inside the element.

### Tailwind vs Bootstrap

One of the pros of Tailwind is its flexibility and freedom, which supports unique designs from the developers. Bootstrap offers a "ready-made" feel to the website, so it's not as customizable as Tailwind.

Bootstrap can be used if the developer does not want to design a website from scratch. Tailwind can be used if the developer wants more freedom designing the website.

</details>