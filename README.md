# [Inventaris](https://oka-inventaris.adaptable.app/)
#### Muhammad Oka - 2206046784

## Assignment Steps
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

## Django Web App Diagram

## The Purpose of Virtual Environment

## MVC, MVT, MVVM