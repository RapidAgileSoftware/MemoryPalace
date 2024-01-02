from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from casting.models import Actor


def index(request):
    context = {
        'actors_list': Actor.objects.order_by(),
    }
    return render(request, "casting/index.html", context)


def detail(request, actor_id):
    actor = get_object_or_404(Actor, pk=actor_id)
    return render(request, 'casting/details.html', {"actor": actor})


def rehearsal(request):
    if request.method == 'POST':
        try:
            rehearsalInput = request.POST["rehearsal_input"]
        except KeyError:
            return render(
                request,
                'casting/index.html',
                {
                    "error_message": "No rehearsal data provided.",
                    'actors_list': Actor.objects.order_by()
                })
        return render(
            request,
            'casting/index.html',
            {
                "rehearsal_result": rehearsalInput,
                'actors_list': Actor.objects.order_by()
            }
        )

    return HttpResponse(request)
