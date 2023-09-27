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