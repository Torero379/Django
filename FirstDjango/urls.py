
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('item/<int:item>', views.item1),
    path('items', views.all_items)
]
