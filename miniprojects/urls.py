from django.urls import path, include
from . import views

app_name = 'miniprojects'

urlpatterns = [
    ########################################################################
    path('', views.index, name='miniprojects-index'),

    # posts urls for crud operations
    path('miniprojects/', views.MiniprojectList.as_view(), name='miniproject-list'),
    path('miniprojects/<int:tag_id>', views.MiniprojectListByTag.as_view(), name='miniproject-list'),
    path('miniproject/add/', views.MiniprojectCreate.as_view(), name='miniproject-add'),
    path('miniproject/<int:pk>/detail/', views.MiniprojectDetail.as_view(), name='miniproject-detail'),
    path('miniproject/<int:pk>/update/', views.MiniprojectUpdate.as_view(), name='miniproject-update'),
    path('miniproject/<int:pk>/delete/', views.MiniprojectDelete.as_view(), name='miniproject-delete'),

]

