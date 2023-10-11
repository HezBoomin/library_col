import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from main.forms import ProductForm
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
# Create your views here.
def show_main(request):
    items = Item.objects.filter(user=request.user)
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
        
    item_count = items.count()
    context = {
        'username': request.user.username,
        'app_name': 'Library Collection',
        'class' : 'PBP KKI',
        'items': items,
        # 'total': total,
        'item_count': item_count,
        'last_login': request.COOKIES['last_login'],
               }
    return render(request, 'main.html', context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

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



def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# delete item
def delete_item(request, id):
    item = Item.objects.get(pk=id)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))




def get_product_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount= request.POST.get("amount")
        description = request.POST.get("description")
        categories = request.POST.get("categories")
        user = request.user     
        new_item = Item(name=name, amount=amount, description=description, user=user, categories=categories)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_item_ajax(request, id):
    item = Item.objects.get(pk=id)
    item.delete()
    return HttpResponse(b"DELETED", status=201)

@csrf_exempt
def increment_item_ajax(request, id):
    item = Item.objects.get(pk=id)
    item.amount += 1
    item.save()
    return HttpResponse(b"DELETED", status=201)

@csrf_exempt
def decrement_item_ajax(request, id):
    item = Item.objects.get(pk=id)
    item.amount -= 1
    item.save()
    return HttpResponse(b"DELETED", status=201)