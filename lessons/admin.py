from django.contrib import admin
from .models import Lesson

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title',)
    # list_filter = ('status' 'created' 'publish' 'author')
    # search_fields = ('title' 'body')
    # prepopulated_fields = {'slug' ('title' )}
    # raw_id_fields = ('author')
    # date_hierarchy = 'publish'



