from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def home(request):
    return render(request, "index.html", {})

def result(request):
    if request.method == "POST":
        return render(request, "result.html", {})
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')