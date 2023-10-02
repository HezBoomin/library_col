<details>
<summary>Assignment 2</summary>

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

</details>

<details>
<summary>Assignment 3</summary>

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

</details>

<details>
<summary>Assignment 4</summary>

# Assignment 4

## Answers

### What is UserCreationForm in Django? Explain its advantages and disadvantages.
Django UserCreationForm is used for creating a new user that can use our web application. It has three fields: username, password1, and password2(which is basically used for password confirmation). It advantage is really simple to use and have it's own template for the registration form. It disadvantage is it have limited fields. Suppose we want to send the verification mail to verify the User; we cannot do that because it doesn't have an email field.

### What is the difference between authentication and authorization in Django application? Why are both important?
Authentication verifies a user is who they claim to be, and authorization determines what an authenticated user is allowed to do. Authentication and authorization are two vital information security processes that administrators use to protect systems and information. Authentication verifies the identity of a user or service, and authorization determines their access rights.

### What are cookies in website? How does Django use cookies to manage user session data?
Cookies are text files with small pieces of data that are used to identify your computer as you use a network. Django uses a cookie containing a special session id to identify each browser and its associated session with the site. The actual session data is stored in the site database by default.

### Are cookies secure to use? Is there potential risk to be aware of?
Cookies themselves are not inherently secure or insecure; their security depends on how they are used and implemented. Cookies are small pieces of data that websites store on a user's device to track information or maintain session data. The potential risk is cybercriminals can steal sensitive data from cookies if the cookies are not secured.

### Show information of logged-in user
<img src="/assets/hez-login.png">
<img src="/assets/bobi-login.png">

### Explain how you implemented the checklist above step-by-step (not just following the tutorial).
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

</details>

<details open>
<summary>Assignment 5</summary>

# Assignment 5

## Answers

### Explain the purpose of some CSS element selector and when to use it.

1. Element Selector
    The purpose is to Selects all HTML elements of a specific type. We use this selector when we want to apply a style to all instances of a particular HTML element throughout our website. Example: `p` selector targets all `<p>` (paragraph) elements.
2. Class Selector
    The purpose is to Selects elements with a specific class attribute value. We Use this selector when we want to apply a style to one or more elements with a specific class. Classes can be reused on multiple elements. Example: `.btn` selector targets all elements with `class="btn"`.
3. ID Selector
    The purpose is to  Selects a single element with a specific `id` attribute value. We use this selector when we want to target a unique element with a specific `id`. Example: `#header` selector targets the element with `id="header"`.

### Explain some of the HTML5 tags that you know.

- `<header>` : Represents the header of a document or a section.
- `<svg>` : Embed SVG (Scalable Vector Graphics) content in an HTML document.
- `<time>` : Represents a time and/or date.

###  What are the differences between margin and padding?

Padding represents the amount of inner space an element has, while the margin is whitespace available surrounding an element.

### What are the differences between the CSS framework Tailwind and Bootstrap? When should we use Bootstrap rather than Tailwind, and vice versa?

Tailwind is a css framework with extensive flexiblity and freedom. It's offer a lot of customization but has a steeper learning curve. Bootstrap provides a more opinionated and structured development experience with a wide range of pre-built components. It's not as flexible as bootstrap but it is really easy to get a grip of. We should use bootstrap when we want to make a simple website that doesn't require many customization for its css. We should use Tailwind if we want to make a more extensive website with a lot of customization on it's css.

### Explain how you implemented the checklist above step-by-step (not just following the tutorial)

1. Install Compressor and Tailwind into Django
    
    We need to install Compressor to compress the html and js file with

    ```
    python -m pip install django-compressor

    ```

    Then we put `compressor` inside `INSTALLED_APPS` inside `settings.py`

    To install Tailwind into Django there's a couple of steps. First we need to Run the following command the install Tailwind CSS as a dev dependency using NPM:

    ```
    npm install -D tailwindcss
    ```

    then we create a new `tailwind.config.json` file with this command:

    ```
    npx tailwindcss init
    ```

    inside `tailwind.config.json` we put `'./library_col/**/*.{html,js}', './static/**/*.{html,js}', './templates/**/*.{html,js}', './main/**/*.{html,js}'` inside the content list. Next we create new folder name `static` in root directory with folder `css` and `src` inside of it. Inside `src` we create file `input.css` the we put these code inside of it
    
    ```css
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    ```

    inside `package.json` we add

    ``` json
    "scripts": {
    "dev": "tailwindcss -i static/src/input.css -o static/css/output.css --watch"
     }
    ```

    then we put thses lines of command inside `base.html` inside `head` class below meta block
    ```html
    {% compress css %}
    <link rel="stylesheet" href="{% static 'css/output.css' %}">
    {% endcompress %}
    ```

    Then we run the command `npm run dev` to start tailwind.

2. Customize `main.html`

    ```html
    {% extends 'base.html' %}
    {% block content %}
    <div class="">
        <nav class="bg-gray-800">
            <div class="mx-auto">
                <div class="relative flex h-16 items-center justify-between">
                    <div class="flex space-x-4 justify-start">
                        <a href="{% url 'main:show_main' %}" class=" text-white rounded-md px-4 py-2 text-sm font-medium text-xl">
                            {{ app_name }}
                        </a>
                    </div>
                    <div class="relative px-3 py-3">
                        <a href="{% url 'main:logout' %}" class="py-2 text-sm font-medium rounded-md pl-20">
                            <button class="bg-gray-900 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full">
                                Logout
                            </button>
                        </a>
                    </div>
                </div>
            </div>
        </nav>

        <div class="mx-auto relative py-4 px-4 pb-20 text-center">
            <h1 class="text-3xl font-bold">Hello There</h1>
            <h1 class="text-7xl font-bold pr-2">{{ username }}!</h1> <!-- Change it to your name -->
            <h1 class="text-xl ">From Class {{ class }}</h5>
        </div> 
        <div class="px-4 pb-4 flex">
            <a href="{% url 'main:create_product' %}">
                <button class="bg-gray-700 hover:bg-blue-700 text-white font-bold py-2 px-4 mx-1 rounded-full">
                    Add New Book to Collection
                </button>
            </a>
            <p class="px-4 pt-2">You have saved {{ item_count }} books in this application</p>
        </div>
        <div class="relative flex"> 
        {% for item in items %}
            <div class="px-4 w-72">
            {% if forloop.last %}
            <div class=" max-w-sm p-4 bg-white border border-gray-200 rounded-lg shadow dark:bg-blue-900 dark:border-blue-900">
                <h5 class="font-bold text-xl py-2">{{item.name}}</h5>
                <p class="pb-2">Category: {{item.categories}}</p>
                <p class="">Description: </p>
                <div class=" overflow-y-auto max-h-6 pb-10 scrollbar scrollbar-thumb-gray-900 scrollbar-track-gray-900 scrollbar-medium" >
                    <p >{{item.description}}</p>
                </div>
                <p class="py-2">Amount: </p>
                <div class="relative flex">
                    <p class="pr-16 pt-1.5">{{item.amount}}</p>
                    <form method="post" class="">
                        {% csrf_token %}
                        <button class="bg-gray-900 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded-full " type="submit" name="increment" value="{{ item.id }}">
                            +
                        </button>
                        <button class="bg-gray-900 hover:bg-blue-700 text-white font-bold py-1 px-2 mx-1 rounded-full" type="submit" name="decrement" value="{{ item.id }}">
                            -
                        <button class="bg-gray-900 hover:bg-blue-700 text-white font-bold py-2 px-2 mx-1 rounded-full" type="submit" name="delete" value="{{ item.id }}">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
                                <path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>
                            </svg>
                        </button>
                    </form>
                </div>
                <p class="pt-4 text-[12px]">Date Added: {{item.date_added}}</p>
                
            </div>
            {% else %}
                <div class=" max-w-sm p-4 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
                    <h5 class="font-bold text-xl py-2">{{item.name}}</h5>
                    <p class="pb-2">Category: {{item.categories}}</p>
                    <p class="">Description: </p>
                    <div class=" overflow-y-auto max-h-6 pb-10 scrollbar scrollbar-thumb-gray-900 scrollbar-track-gray-900 scrollbar-medium" >
                        <p >{{item.description}}</p>
                    </div>
                    <p class="py-2">Amount: </p>
                    <div class="relative flex">
                        <p class="pr-16 pt-1.5">{{item.amount}}</p>
                        <form method="post" class="">
                            {% csrf_token %}
                            <button class="bg-gray-900 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded-full " type="submit" name="increment" value="{{ item.id }}">
                                +
                            </button>
                            <button class="bg-gray-900 hover:bg-blue-700 text-white font-bold py-1 px-2 mx-1 rounded-full" type="submit" name="decrement" value="{{ item.id }}">
                                -
                            <button class="bg-gray-900 hover:bg-blue-700 text-white font-bold py-2 px-2 mx-1 rounded-full" type="submit" name="delete" value="{{ item.id }}">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
                                    <path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>
                                </svg>
                            </button>
                        </form>
                    </div>
                    <p class="pt-4 text-[12px]">Date Added: {{item.date_added}}</p>
                    
                </div>
            {% endif %}
            </div>
            {% endfor %}
        </div>

        <br />
        <div class="px-4 pt-20 text-center">
            <h5 class="text-sm">Last login session: {{ last_login }}</h5>
        </div>
    </div>

    {% endblock content %}

    ```

3. Customize `register.html`

    ```html
    {% extends 'base.html' %}

    {% block meta %}
        <title>Register</title>
    {% endblock meta %}

    {% block content %}  


    <div class="login flex h-screen justify-center items-center">
        <div class=" flex-col item-center justify-center max-w-sm relative">
            <div class=" p-4 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
                <h1 class="text-center text-4xl pb-3 pt-2">Register</h1>
                <form class="py-2 px-2"  method="POST" action="">
                    {% csrf_token %}
                    <table>
                        <tr>
                            <td class="text-[19px] ">Username: </td>
                            <td class="px-2 text-black"><input type="text" name="username" placeholder="Username" class="form-control"></td>
                        </tr>
                                
                        <tr>
                            <td class="text-xl">Password: </td>
                            <td class="px-2 text-black"><input type="password" name="password1" placeholder="Password" class="form-control"></td>
                        </tr>

                        <tr>
                            <td class="text-[10.5px]"> Confirm Password: </td>
                            <td class="px-2 text-black"><input type="password" name="password2" placeholder=" Confirm Password" class="form-control"></td>
                        </tr>
            
                        <tr>
                            <td></td>
                            <td class="py-2"><input class="btn login_btn bg-gray-900 hover:bg-blue-700 text-white font-bold py-1 px-3 mx-1 rounded-full" type="submit" value="Register"></td>
                        </tr>
                    </table>
                </form>     
                <p class="text-sm">Already have an account? <a class="underline underline-offset-2 hover:text-blue-400" href="{% url 'main:login' %}">Login Now</a></p>    
            </div>
            <div class="my-2 absolute flex items-center justify-center">
                {% if messages %}
                    <ul>
                        {% for message in messages %}
                            <li class="px-2 text-sm text-center">{{ message }}</li>
                        {% endfor %}
                    </ul>
                {% endif %}
                {% if form.errors.username %}
                    <ul>
                        <li class=" px-2 text-sm text-center ">{{ form.errors.username }}</li>
                    </ul>
                {% endif %}        
                {% if form.errors.password1 %}
                    <ul>
                        <li class=" px-2 text-sm text-center">{{ form.errors.password1 }}</li>
                    </ul>
                {% endif %}        
                {% if form.errors.password2 %}
                    <ul>
                        <li class="px-2 text-sm text-center">{{ form.errors.password2 }}</li>
                    </ul>
                {% endif %}   
            </div>
        </div>

    </div>

    {% endblock content %}
    ```

4. Customize `login.html`

    ```html
    {% extends 'base.html' %}

    {% block meta %}
        <title>Login</title>
    {% endblock meta %}

    {% block content %}

    <div class="login flex h-screen justify-center items-center">
        <div class="flex-col item-center justify-center max-w-sm relative">
            <div class=" p-4 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
                <h1 class="text-center text-4xl pb-3 pt-2">Login</h1>
                <form class="py-2 px-2"  method="POST" action="">
                    {% csrf_token %}
                    <table>
                        <tr>
                            <td class="text-[19px] ">Username: </td>
                            <td class="px-2 text-black"><input type="text" name="username" placeholder="Username" class="form-control"></td>
                        </tr>
                                
                        <tr>
                            <td class="text-xl">Password: </td>
                            <td class="px-2 text-black"><input type="password" name="password" placeholder="Password" class="form-control"></td>
                        </tr>
            
                        <tr>
                            <td></td>
                            <td class="py-2"><input class="btn login_btn bg-gray-900 hover:bg-blue-700 text-white font-bold py-1 px-3 mx-1 rounded-full" type="submit" value="Login"></td>
                        </tr>
                    </table>
                </form> 
                <p class="text-sm">Don't have an account yet? <a class="underline underline-offset-2 hover:text-blue-400" href="{% url 'main:register' %}">Register Now</a></p>
            </div>
            <div class="my-2 absolute flex items-center justify-center">
                {% if messages %}
                <ul>
                    {% for message in messages %}
                        <li class="px-2 text-sm text-center">{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}    
            </div>
        </div>

    </div>

    {% endblock content %}
    ```

5. Customize `create_product.html`

    ```html
    {% extends 'base.html' %} 

    {% block content %}

    <div class="login flex h-screen justify-center items-center">
        <div class="flex-col item-center justify-center relative">
            <div class=" p-4 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
                <h1 class="text-center text-4xl pb-3 pt-2">Add New Book</h1>
                <form method="POST">
                    {% csrf_token %}
                    <div class="grid grid-cols-4 gap-2">
                        <label for="id_name" class="font-medium">Name:</label>
                        <input type="text" name="name" maxlength="100" required id="id_name" class="form-control text-black">
                        <label for="id_amount" class="font-medium">Amount:</label>
                        <input type="text" name="amount" required id="id_amount" class="form-control text-black ">
                        <label for="id_amount" class="font-medium">Description:</label>
                        <textarea name="description" cols="40" rows="10" required id="id_description" class="form-control text-black "></textarea>
                        <label for="id_category" class="font-medium">Category:</label>
                        <input type="text" name="categories" maxlength="100" required id="id_category" class="form-control text-black ">
                    </div>
                    <div class="mr-5 py-2 pt-4">
                        <input class="btn login_btn bg-gray-900 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded-full" type="submit" value="Add Book">
                    </div>
                </form>
            </div>
        </div>
    </div>

    {% endblock %}
    ```

6. Customize web scroll bar
    
    To customize the scrollbar i put some line of codes inside `input.css`

    ```css
    @layer utilities {
        .scrollbar::-webkit-scrollbar {
        width: 10px;
        height: 10px;
        }
    
        .scrollbar::-webkit-scrollbar-track {
        border-radius: 100vh;
        background: #f7f4ed;
        }
    
        .scrollbar::-webkit-scrollbar-thumb {
        background: #111827;
        border-radius: 100vh;
        border: 1px solid #f6f7ed;
        }
    
        .scrollbar::-webkit-scrollbar-thumb:hover {
        background: #1d4ed8;
        }
    }

</details>


