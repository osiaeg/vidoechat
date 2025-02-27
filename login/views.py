from django.http.request import HttpRequest
from django.shortcuts import HttpResponse, render


def login(request: HttpRequest):
    if request.method == "POST":
        return HttpResponse(f"{request.POST['username']}, {request.POST['password']}")

    return render(request, "login/login.html")
