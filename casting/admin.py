from django.contrib import admin

from casting.models import Actor, Cast, Role


class RoleAdmin(admin.ModelAdmin):
    list_display = ['acts_as', 'actor']
    fields = ['actor', 'acts_as']


class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'prop', 'activity']


class CastAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Actor, ActorAdmin)
admin.site.register(Cast, CastAdmin)
admin.site.register(Role, RoleAdmin)
