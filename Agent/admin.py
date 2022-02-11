from django.contrib import admin
from Agent.models import Agent, Weekend


# Register your models here.
# class Weekendinline(admin.StackedInline):
#     model = Weekend
#     extra =1

class Weekendinline(admin.TabularInline):
    model = Weekend
    extra = 1


class WeekendAdmin(admin.ModelAdmin):
    fields = ['Agent', 'start_time']
    list_display = ['Agent']
    list_filter = ['Agent']
    search_fields = ['Agent__first_name']
    autocomplete_fields = ['Agent']


class AgentAdmin(admin.ModelAdmin):
    # fields = ['first_name', 'last_name']
    list_display = ['first_name', 'last_name']
    list_display_links = ['first_name']
    fieldsets = (
        ('General',
         {'fields': ['first_name', 'last_name', 'count_Weekend']}),
        ('Info', {'fields': ['descriptions', 'experience_year', 'count_service', 'image']})
    )
    search_fields = ['first_name']
    inlines = [Weekendinline]

    # def count_Weekend(self, obj: Agent):
    #     return obj.Weekend_set.count()


admin.site.register(Agent, AgentAdmin)
admin.site.register(Weekend, WeekendAdmin)
