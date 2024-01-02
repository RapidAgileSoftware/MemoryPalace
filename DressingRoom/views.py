import django.http


def index(request):
    return django.http.HttpResponse("Welcome to the dressing Room")
