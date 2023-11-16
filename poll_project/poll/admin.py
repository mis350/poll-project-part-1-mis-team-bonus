from django.contrib import admin


# Register your models here.

class PollAdmin(admin.ModelAdmin):

    list_display = ['title', 'question', 'status', 'active_untill']
    list_filter = ('title', 'active_untill')
    search_fields = ['title', 'question']


from .models import Poll, Option, Response
# Register your models here.

admin.site.register(Poll)
admin.site.register(Option)
admin.site.register(Response)