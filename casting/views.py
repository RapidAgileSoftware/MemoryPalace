from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from casting.models import Actor


def index(request):
    context = {
        'actors_list': Actor.objects.order_by()[:10],
    }
    return render(request, "casting/index.html", context)


def detail(request, actor_id):
    actor = get_object_or_404(Actor, pk=actor_id)
    return render(request, 'casting/details.html', {"actor": actor})


def rehearsal(request, actor_id, prop_id, action_id):
    return HttpResponse("It actor %s with prop %s doing %s" % (actor_id, prop_id, action_id))
