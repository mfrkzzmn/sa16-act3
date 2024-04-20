from django.shortcuts import render


def index(request):
    return render(request, "portfolio/index.html")


def about(request):
    return render(request, "portfolio/about.html")


def work(request):
    return render(request, "portfolio/work.html")


def contact(request):
    return render(request, "portfolio/contact.html")
