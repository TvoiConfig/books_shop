from django.shortcuts import render
from django.views.generic import FormView
from .models import *
from .forms import RecordForm

def index(request):
    return render(request, 'main/index.html')

def about(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RecordForm()
        
    return render(request, 'main/about.html', {'form': form})

def shop(request):
    product = Products.objects.all()
    return render(request, 'main/shop.html', {'product': product})
