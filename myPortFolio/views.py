from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "index.html")

# def about(request):
#     return HttpResponse("About Page")

# def portfolio(request):
#     return HttpResponse("Portfolio Page")

# def blog(request):
#     return HttpResponse("Blog Page")

# def contact(request):
#     return HttpResponse("Contact Page")

