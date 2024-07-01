from django.shortcuts import render, HttpResponse
# Create your views here.

def index(request):
    context = {
        'info':"Samir"
    }
    # return HttpResponse("This is home page!")
    return render(request, "index.html", context)

def about(request):
    return HttpResponse("This is About page!")

def services(request):
    return HttpResponse("This is Services page!")

def contact(request):
    return HttpResponse("This is Contact page!")