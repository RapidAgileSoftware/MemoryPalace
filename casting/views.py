from django.http import HttpResponse


def index(request):
    return HttpResponse("This is the CASTING index page")


def detail(request, actor_id):
    return HttpResponse("You are looking at the details of actor {}".format(actor_id))


def rehearsal(request, actor_id, prop_id, action_id):
    return HttpResponse("It actor %s with prop %s doing %s" % (actor_id, prop_id, action_id))
