from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from api import models as db_model
# Create your views here.
ans = ''

def home(request):
    if request.method == "POST":
        url_recieved = request.POST.get("incoming_url")
        
        if url_recieved not in db_model.list_of_objects_short.keys():
            ans = db_model.create_short_url(url_recieved)
            return render(request, "result.html", {'ans' : ans})
        else:
            # the url already present in the DB so return present one
            ans = db_model.list_of_objects_short[url_recieved]
            #print("ans is " , ans)
            
            return render(request, "result.html", {'ans' : ans})

    return render(request, "index.html", {})

def result(request):
    if request.method == "POST":
        url_recieved = request.POST.get("incoming_url")
        
        if url_recieved not in db_model.list_of_objects_short.keys():
            ans = db_model.create_short_url(url_recieved)
            #print("-------------------->", ans)
            origional_link = db_model.list_of_objects_long[ans]
            return render(request, "result.html", {'ans' : ans, 'origional_link' : origional_link })
        else:
            # the url already present in the DB so return present one
            ans = db_model.list_of_objects_short[url_recieved]
            #origional_link = ans.split('/')[1]
            origional_link = db_model.list_of_objects_long[ans]
            return render(request, "result.html", {'ans' : ans, 'origional_link' : origional_link})
        return render(request, "result.html", {})
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')


def redirection_function(short_url):
    long_url = db_model.list_of_objects_long[short_url]
    if long_url:
        return redirect(long_url)
    return HttpResponseNotFound('<h1>Page not found</h1>')
