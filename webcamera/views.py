# from django.http import HttpResponse
from django.shortcuts import render


def camera(request):
    # return HttpResponse("Hello world.")
    return render(request, "index.html")
