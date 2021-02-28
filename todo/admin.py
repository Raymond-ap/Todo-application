from django.contrib import admin
from .models import Todo, Status


class TodoAmin(admin.ModelAdmin):
    list_display = ('title','status','created')

admin.site.register(Todo, TodoAmin)
admin.site.register(Status)