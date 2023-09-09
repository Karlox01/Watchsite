from django.urls import path

from . import views 

app_name = 'watches'

urlpatterns = [
    path('', views.items, name='items'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/submit_offer/', views.submit_offer, name='submit_offer'),
    path('watches/category/<str:category_name>/', views.watches_by_category, name='watches_by_category'),
    path('watches/filter/price/', views.filtered_watches_by_price, name='filtered_watches_by_price'),
]