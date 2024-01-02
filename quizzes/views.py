import django.http


def index(request):
    return django.http.HttpResponse("Hello world, this is a Memory Quiz")
