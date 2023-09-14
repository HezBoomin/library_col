# Assignment 2

## APP
Here is the link to my [APP](https://library-collection.adaptable.app/main/)

## Answers

### 1. How do you implement the tasks in the checklist?
1. Create a new Django Project
    - To create a new Django Project first we need to create a virtual environment
    ```
    python -m venv env
    ```
    - Then activate the virtual environment
    ```
    env\Scripts\activate
    ```
    - In the same directory I create a file named `requirements.txt` and add some dependecies.
    - Then run the command `pip install -r requirements.txt` to install the dependencies
    - Then start the project by run the command `django-admin startproject library_col .`
    - For deployment purposes add `"*"` to `ALLOWED_HOSTS` in `settings.py`
    - I add a `.gitignore` file
2. Create an app with the name `main`.
    - Run the command `python manage.py startapp main` to make `main` app
    - Create folder `templates` inside `main` and add `main.html` inside the folder
3. Create a URL routing configuration to access the `main` app.
    - in `urls.py` inside `library_col` add `path('main/', include('main.urls'))`
4. Create a model on the `main` app with name `Item` and add some mandatory attributes
    - In `models.py` i add an app name `Item` with attributes such as:
        - `name`
        - `date_added`
        - `amount`
        - `description`
        - `categories`
5. Create a function in `views.py` that returns an HTML template containing my application name, your name, and your class.
    - in `views.py` I add function `show_main` with context _application name_, _my name_, _my class_. Then render the context to `main.html`
    - In `main.html` I can call each item in context with `{{ name }}` for example. I added the 3 item
6. Create a routing in `urls.py` to map the function in `views.py` to an URL
    - in `main.py` create `urls.py` and add ` app_name = `main` `. Add `path('', show_main, name='show_main')` to a list variable name `urlpatterns`
7. Deploy the app to adaptable
    - Add, commit, push the project to a repository named library_col 
    - Deploy it in adaptable

### 2. Create a diagram explaining the flow of client requests to a Django web app and its response.
<img src="/assets/flowchart.png">

### 3. What is the purpose of a virtual environment? Can we create a Django web app without a virtual environment?
The purpose of virtual environment isolate the dependencies and libraries required for a specific project. It is possible to create a Django web without a virtual environment, but in some case it is better to use a virtual environment. For example in project A we use Django version 4.0 and we want to make project B with Django version 4.1. If we install Django without virtual environment, the Django will be updated to version 4.1 on project A. In such situations virtual environment can be really useful to maintain the dependencies of both projects.

### 4. What is MVC, MVT, and MVVM? Explain the differences between the three.
MVC is Model-View-Controller. In MVC, Model Stores data and application logic, View displays data from Model, and Controller Acts as an intermediary between the model and view. MVT is Model-View-Template. In MVT, Model Stores data and application logic, View displays data from Model and connects it to the template, and Template Determines the user interface's appearance. MVVM is Model-View-ViewModel. IN MVVM, Model Stores data and application logic, View displays data from Model, and ViewModel transforms data from the Model into a format that the View can easily display and interact with.MVC and MVT are similar, with the primary difference being the terminology used and the specific implementation details in their respective frameworks. MVVM introduces a clear separation between the View and ViewModel, with an emphasis on data binding and two-way communication between them.

# Assignment 3

## Answers

### What is the difference between POST form and GET form in Django?
The Difference is on the usage between those two. POST is used if the request makes changes in the database or in otherwise we use POST to send data to the database. GET is only used only for requests that do not affect the state of the system or in otherwise we use GET to retrieve data from the database without altering it.

### What are the main differences between XML, JSON, and HTML in the context of data delivery?
HTML is the primary building block of web development and is used to define the structure of a page. While JSON and XML is used to transport data between servers, it have differences between those two. XML is suitable for structured and self-describing data, JSON is preferred for lightweight data interchange and JavaScript integration.

### Why is JSON often used in data exchange between modern web applications?
Many modern web applications use JSON because its simplicity, efficiency, compatibility with JavaScript, and readability. JSON is easy to write and understand, does not require any special tags, attributes, or schemas, unlike XML. JSON also can be used with other languages, so it's useful for data exchange between systems.

### Explain how you implemented the checklist above step-by-step (not just following the tutorial).
1. Create `forms.py` inside the `main` folder.

    Inside the file `forms.py` we create a class `ProductForm` for the form by using `ModelForm` as parameter. Inside the class we create a `META` class containing `model = Item` to point to a model used by the form. It also contain `fields = ["name", "price", "description"]` to be used to select attributes of the model `Item`.
2. Create `create_product` object inside views.py

    Inside the file `views.py` we create function `create_product` that accept a parameter request. In `create_product` we create a new `ProductForm` filled with user input in `request.POST` as a `QueryDict`. Then we validate the content by using `form.is_valid()` and save the content by using `form.save()`. If the content is saved, go back to the main page by using `return HttpResponseRedirect(reverse('main:show_main'))`. the function will render `create_product.html`.
3. Change the `show_main` function inside `views.py`

    add `items = Item.objects.all()` to fetch all `item` object from the application's database.
4. Create URL routing for `create_product`

    in `urls.py` inside `library_col` add `path('create-product', create_product, name='create_product'),`.
5. Create a `create_product.html` inside `templates` folder inside the `main` folder

    Fill the HTML file with appropriate code to display the form as table, used `{% csrf_token %}` as a security, and used `<form method="POST">` to tag the form with `POST` method.
6. Create object `show_xml` and create the URL routing for it

    Fetched `Item` objects and return as XML by using 
    ```py
    def show_xml(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
    in `urls.py` inside `library_col` add `path('show_xml/', show_xml, name='show_xml'),`.
7. Create object `show_json` and create the URL routing for it

    Fetched `Item` objects and return as XML by using 
    ```py
    def show_json(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
    in `urls.py` inside `library_col` add `path('show_json/', show_json, name='show_json'),`.
8. Create object `show_xml_by_id` and create the URL routing for it

    Fetched `Item` objects and return as XML by using 
    ```py
    def show_xml_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
    in `urls.py` inside `library_col` add `path('show_xml_by_id/', show_xml_by_id, name='show_xml_by_id'),`.
9. Create object `show_json_by_id` and create the URL routing for it

    Fetched `Item` objects and return as XML by using 
    ```py
    def show_json_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
    in `urls.py` inside `library_col` add `path('show_json_by_id/', show_json_by_id, name='show_json_by_id'),`.

### Access the five URLs in point 2 using Postman, take screenshots of the results in Postman, and add them to README.md.
<img src="/assets/show_main.png">
<img src="/assets/show_xml.png">
<img src="/assets/show_json.png">
<img src="/assets/show_xml_by_id.png">
<img src="/assets/show_json_by_id.png">
        