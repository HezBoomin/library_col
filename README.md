# Assignment 2

## APP
Here is the link to my [APP](https://library-collection.adaptable.app/main/)

## Answers

### How do you implement the tasks in the checklist?

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
            -`name`
            -`date_added`
            -`amount`
            -`description`
            -`categories`
    5. Create a function in `views.py` that returns an HTML template containing my application name, your name, and your class.
        - in `views.py` I add function `show_main` with context _application name_, _my name_, _my class_. Then render the context to `main.html`
        - In `main.html` I can call each item in context with `{{ name }}` for example. I added the 3 item
    6. Create a routing in `urls.py` to map the function in `views.py` to an URL
        - in `main.py` create `urls.py` and add ` app_name = `main` `. Add `path('', show_main, name='show_main')` to a list variable name `urlpatterns`
    7. Deploy the app to adaptable
        - Add, commit, push the project to a repository named library_col 
        - Deploy it in adaptable

    

        