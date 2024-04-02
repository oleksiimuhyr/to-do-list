from django.contrib import admin

from catalog.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "creation_date", "deadline", ]
    search_fields = ["content", ]


admin.site.register(Tag)
