# from django.http import HttpResponse
from django.shortcuts import render
# from random import randint
# Create your views here.

def index(request):
    # ramdom_number = randint(1, 10)
    # return HttpResponse("Hello, world. {}".format(ramdom_number) )
    # return HttpResponse("Hello, world. You`re at the index")
    name = "dong ju"
    return render(request, "index.html", { "name" : name })
