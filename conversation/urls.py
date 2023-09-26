from django.urls import path

from . import views
from .views import delete_conversation

app_name = 'conversation'


urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/<int:item_pk>/', views.new_conversation, name='new'),
    path('conversation/<int:pk>/delete/', delete_conversation, name='delete_conversation'),
]