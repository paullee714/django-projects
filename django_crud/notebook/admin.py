from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
# Register your models here.
from .models import Notebook

@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'note_data',
        'draft_user',
        'created_at',
        'updated_at',
    ]

    list_display_links = ['id','note_data','draft_user']
    list_filter = ['draft_user',('created_at',DateRangeFilter),('updated_at',DateRangeFilter)]