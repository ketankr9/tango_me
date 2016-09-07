from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    content_dict={'boldmessage':"Crunchy,creamy,cookie,candy,cupcake!",'count':45}
    return render(request,'rango/index.html',context=content_dict)
def about(request):
    return HttpResponse("<h2>Rango says this is the about page</h2><a href='/'>IndexPage</a>")
def rangoo(request):
    return HttpResponse("<h1>Rango page</h2><br/>")
