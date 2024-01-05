from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404
from django.views import generic

from casting.models import Actor, Cast


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
    roles = cast.roles.all()

    context = {
        'activeCast': cast,
        'activeRoles': roles
    }

    if request.method != "POST":
        return render(request, "casting/rehearsal.html", context)

    try:
        context['rehearsal_result'] = create_characters(request.POST['code_sequence'], roles)
    except (KeyError, TypeError, ValidationError):
        context['error_message'] = "Invalid Code Sequence"

    return render(request, "casting/rehearsal.html", context)


def create_characters(code_sequence, roles):
    # Validate code_sequence
    if validate_code_sequence(code_sequence):
        cast_dict = create_cast_dict(roles)
        character_list = []
        character = {}
        for position, char in enumerate(code_sequence):
            if position % 3 == 0:
                character = {'person': cast_dict[char]['person']}
            if position % 3 == 1:
                character['prop'] = cast_dict[char]['prop']
            if position % 3 == 2:
                character['activity'] = cast_dict[char]['activity']
                character_list.append(character)
        return character_list
    else:
        raise ValidationError("Invalid Code Sequence")


def create_cast_dict(roles):
    cast_dict = {}
    for role in roles:
        actor = role.actor
        cast_dict[role.acts_as] = {'person': actor.name, 'prop': actor.prop, 'activity': actor.activity}
    return cast_dict


def validate_code_sequence(code_sequence):
    return len(code_sequence) % 3 == 0 and code_sequence.isnumeric()
