from django.shortcuts import render

def home(request):
    return render(request, "home.html", {})


def about(request):
    return render(request, "about.html", {})


def services(request):
    return render(request, "services.html", {})


def contact(request):
    return render(request, "contact.html", {})


def document(request):
    return render(request, "document.html", {})

def ecommerce(request):
    return render(request, "ecommerce.html", {})

def document1(request):
    return render(request, "document1.html", {})

def document2(request):
    return render(request, "document2.html", {})

