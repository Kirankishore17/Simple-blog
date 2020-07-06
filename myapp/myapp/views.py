from django.http import HttpResponse
from django.shortcuts import render
def about(request):
    return HttpResponse("about page")


def home(request):
    # ob = {}
    # ob.message = "home page rendered"
    # ob.list = [i**2 for i in range(1,5)]
    return render(request, "home.html" )