from django.urls import path, include
from . import views

app_name = 'lessons'

urlpatterns = [
    ########################################################################
    path('', views.index, name='lessons-index'),

    # posts urls for crud operations
    path('lessons/', views.LessonList.as_view(), name='lesson-list'),
    path('lessons/<int:tag_id>', views.LessonListByTag.as_view(), name='lesson-list'),
    path('lesson/add/', views.LessonCreate.as_view(), name='lesson-add'),
    path('lesson/<int:pk>/detail/', views.LessonDetail.as_view(), name='lesson-detail'),
    path('lesson/<int:pk>/update/', views.LessonUpdate.as_view(), name='lesson-update'),
    path('lesson/<int:pk>/delete/', views.LessonDelete.as_view(), name='lesson-delete'),

]


