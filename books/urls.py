from django.urls import path

from . import views

urlpatterns = [ 
    path('', views.chooseBook, name='chooseBook'),
    path('bookInfo/<str:pk>', views.bookInfo, name='bookInfo'),
]