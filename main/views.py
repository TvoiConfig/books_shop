from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def shop(request):
    return render(request, 'main/shop.html')

def shop_single(request):
    return render(request, 'main/shop-single.html')
