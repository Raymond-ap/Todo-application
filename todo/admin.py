from django.contrib import admin
from .models import Todo


class TodoAmin(admin.ModelAdmin):
    list_display = ('title','completed','created')

admin.site.register(Todo, TodoAmin)