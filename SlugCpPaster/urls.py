from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.form_viewer, name='slug_form'),
    path('create/', views.slug_creator, name='create_slug'),
    path('<slug:input_slug>/', views.show_content, name='show_content'),
]
