from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Hezekial Octora Yudha Tampubolon',
        'app_name': 'Library Collection',
        'class' : 'PBP KKI'
               }
    return render(request, 'main.html', context)