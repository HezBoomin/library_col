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

# Assignment 4

## Answers

# What is UserCreationForm in Django? Explain its advantages and disadvantages.
Django UserCreationForm is used for creating a new user that can use our web application. It has three fields: username, password1, and password2(which is basically used for password confirmation). It advantage is really simple to use and have it's own template for the registration form. It disadvantage is it have limited fields. Suppose we want to send the verification mail to verify the User; we cannot do that because it doesn't have an email field.

# What is the difference between authentication and authorization in Django application? Why are both important?
Authentication verifies a user is who they claim to be, and authorization determines what an authenticated user is allowed to do. Authentication and authorization are two vital information security processes that administrators use to protect systems and information. Authentication verifies the identity of a user or service, and authorization determines their access rights.

# What are cookies in website? How does Django use cookies to manage user session data?
Cookies are text files with small pieces of data that are used to identify your computer as you use a network. Django uses a cookie containing a special session id to identify each browser and its associated session with the site. The actual session data is stored in the site database by default.

# Are cookies secure to use? Is there potential risk to be aware of?
Cookies themselves are not inherently secure or insecure; their security depends on how they are used and implemented. Cookies are small pieces of data that websites store on a user's device to track information or maintain session data. The potential risk is cybercriminals can steal sensitive data from cookies if the cookies are not secured.

# Show information of logged-in user
<img src="/assets/hez-login.png">
<img src="/assets/bobi-login.png">

# Explain how you implemented the checklist above step-by-step (not just following the tutorial).
1. Create Register Form and Function

    In  `views.py` import `Redirect`, `UserCreationForm`, and `Messages`. Create a `Register` function like the following code:
    ```py
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
    ```
    After creating the function, create a file called `register.html` in template folder inside the main folder to get the register data from the web. Create routing of this function in `urls.py`

2. Create Login Form and Function and Add Lost Login Date to Cookies and Show the Last Login to the Main Page

    In  `views.py` import `authenticate` and `login`. Create a `login_user` function that also get the last login date and add it cookie like the following code:
    ```py
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
    ```
    After creating the function, create a file called `login.html` in template folder inside the main folder toin views.py to login the user. We add `'last_login': request.COOKIES['last_login'],` to `context` to show the last login data in `main.html`. Create routing of this function in `urls.py`
3. Create Logout Form and Function That Also Delete the Last Login From Cookie

    in `views.py` import `logout`. Create a `logout_user` function that also delete the last login from cookie like the following code
    ```py
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    ```
    Create routing of this function in `urls.py`. Add a `logout` button in `main.html` to logout the user

4. Restricting Access to the Main Page if the User Didn't Login

    in `views.py` import `login_required` the put `@login_required(login_url='/login')` above `show_main` function.

5. Connect `Item` Model to `User` Model

    in `models.py` import user, then add `user = models.ForeignKey(User, on_delete=models.CASCADE)` inside existing Item model. Modify `create-product` funtion set the `user` field to the `User` object associated with the currently logged-in user, indicating that the product belongs to that user with the following code:
    ```py
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return HttpResponseRedirect(reverse('main:show_main'))
    ```
    In `show_main` function add `'name': request.user.username` to context. Save all changes and run the migrations for the model.

6. Create 2 User with 3 Item per User

    Just register and login to two user and input 3 data item in each account

7. Make a Increment and Deacrement Button for Amount and Delete Button to Delete the Item

    In `views.py` add the following code:
    ```py
    if request.method == 'POST':
        if 'increment' in request.POST:
            item_id = request.POST.get('increment')
            item = items.get(id=item_id)
            item.amount += 1
            item.save()
            return HttpResponseRedirect(reverse('main:show_main'))
        elif 'decrement' in request.POST:
            item_id = request.POST.get('decrement')
            item = items.get(id=item_id)
            item.amount -= 1
            item.save()
            return HttpResponseRedirect(reverse('main:show_main'))
        elif 'delete' in request.POST:
            item_id = request.POST.get('delete')
            item = items.get(id=item_id)
            item.delete()
            return HttpResponseRedirect(reverse('main:show_main'))
    ```
    In `main.html` create a button to increment,decrement, and delete. `if request.method == 'POST':` This line checks if the HTTP request method used to access the view is POST. `if 'increment' in request.POST:`, `elif 'decrement' in request.POST:`, `elif 'delete' in request.POST:` Those lines  checks if the string `increment` or `decrement` or `delete` exists in the POST data. `item_id = request.POST.get('increment')` , `item_id = request.POST.get('decrement')`, and `item_id = request.POST.get('delete')` is for retrieves the value associated with the `increment`, `decrement`, `delete` button from the POST data when the button of each function is pressed. `item = items.get(id=item_id)` With the item's ID obtained from the POST data, this line fetches the corresponding item from the database. It uses the get method with the id field to retrieve the specific item.`item.amount += 1 and item.save()` to increment amount and save the data, `item.amount -= 1 and item.save()` to decrement amount and save the data, `item.delete()` to delete the item. `return HttpResponseRedirect(reverse('main:show_main'))` After processing the form submission and updating the item's amount, this line redirects the user to the `show_main` view. 