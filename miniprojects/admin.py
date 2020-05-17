from django.contrib import admin
from .models import Miniproject

@admin.register(Miniproject)
class MiniprojectAdmin(admin.ModelAdmin):
    list_display = ('title', 'finished')
    # list_filter = ('status' 'created' 'publish' 'author')
    # search_fields = ('title' 'body')
    # prepopulated_fields = {'slug' ('title' )}
    # raw_id_fields = ('author')
    # date_hierarchy = 'publish'


