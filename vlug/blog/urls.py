from django.urls import path
from . import views

# app_name variable llows to organize URLs by application and use the name when referring to them.
app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail')
]

