from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.get_prompts),
    path('testget/', views.test_get),
    path('post/', views.post_message),
    path('hackathon-chat/', views.hackathon_chat),
    path('hackathon-1-stream/', views.OpenAIStreamView.as_view(), name='hackathon-1-stream'),
]