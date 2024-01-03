from django.shortcuts import get_object_or_404, render

from casting.models import Actor


def index(request):
    context = {
        'actors_list': Actor.objects.order_by(),
    }
    return render(request, "casting/index.html", context)


def detail(request, actor_id):
    actor = get_object_or_404(Actor, pk=actor_id)
    return render(request, 'casting/details.html', {'actor': actor})


def rehearsal(request):

    context = {
        'actors_list': Actor.objects.order_by(),
    }
    if request.method == 'POST':
        try:
            context['rehearsal_result'] = request.POST['rehearsal_input']
        except KeyError:
            context['error_message'] = 'No rehearsal data provided'

    return render(request, "casting/index.html", context)
