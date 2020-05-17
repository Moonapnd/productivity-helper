from django.urls import path, include
from . import views

app_name = 'learningforms'

urlpatterns = [
    ########################################################################
    path('', views.index, name='learningforms-index'),

    # posts urls for crud operations
    path('send_message/', views.SendMessage.as_view(), name='send_message'), 
    # path('send_message_done/', views.SendEmail.as_view(), name='send_message_done'), 

]


