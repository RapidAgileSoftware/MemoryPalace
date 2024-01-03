from django.shortcuts import render, get_object_or_404
from django.views import generic
from casting.models import Actor, Cast, Role


def index(request):
    cast = Cast.objects.first()
    context = {
        'currentCast': cast,
        'currentRoles': cast.roles.all()
    }
    return render(request, "casting/index.html", context)


class IndexView(generic.ListView):
    template_name = "casting/index.html"
    context_object_name = "actors_list"

    def get_queryset(self):
        return Actor.objects.order_by("id")


class DetailView(generic.DetailView):
    model = Actor
    template_name = "casting/details.html"


def rehearsal(request, cast_id):
    cast = get_object_or_404(Cast, pk=cast_id)
    context = {
        'activeCast': cast,
        'activeRoles': cast.roles.all()
    }
    if request.method == 'POST':
        try:
            context['rehearsal_result'] = request.POST['rehearsal_input']
        except KeyError:
            context['error_message'] = 'No rehearsal data provided'

    return render(request, "casting/rehearsal.html", context)
