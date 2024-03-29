from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('new_folder/', views.new_folder, name='new_folder'),
    path('open_folder/<str:pk>/', views.open_folder, name='open_folder'),
    path('upload/', views.upload_file, name='upload_file'),
    path('delete_file/', views.delete_file, name='delete_file'),
    path('delete_folder/<str:pk>', views.delete_folder, name='delete_folder'),
]
