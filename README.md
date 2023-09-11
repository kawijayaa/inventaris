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