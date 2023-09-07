from django.urls import path

from . import views 

app_name = 'watches'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/submit_offer/', views.submit_offer, name='submit_offer'),
]