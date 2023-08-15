from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.get_prompts),
    path('post/', views.post_message),
]