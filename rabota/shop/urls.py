from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns=[
    path('',views.post_list,name='post_list'),
    path('Cveti/<int:pk>',views.post_detail,name='post_detail'),
    path('Cveti/new/',views.post_new,name='post_new'),
]