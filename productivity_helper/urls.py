from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
# to allow serving media files during developement
from django.conf import settings
from django.conf.urls.static import static

def index(request):
    return HttpResponse('Productivity Helper WebSite Work')

urlpatterns = [
    path('', index),
    path('accounts/', include('accounts.urls')),
    path('miniprojects/', include('miniprojects.urls', namespace='miniprojects')),
    path('lessons/', include('lessons.urls', namespace='lessons')),
    # path('learningforms/', include('learningforms.urls', namespace='learningforms')),
    path('admin/', admin.site.urls),
]

# serving media files only during developement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
