from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {"name": "Avanindra",
               "number": 5,
    }
    return render(request, "projects/index.html", context=context)

