from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from api import models as db_model
# Create your views here.
def home(request):
    if request.method == "POST":
        url_recieved = request.form["incoming_url"]
        url_found = db_model.UrlModel.return_long_url
        #print(url_recieved)
        return url_recieved 
    return render(request, "index.html", {})

def result(request):
    if request.method == "POST":
        return render(request, "result.html", {})
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')