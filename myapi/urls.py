from django.urls import path,include
from .views import upload_image, list_images, upload_video, list_videos, RegisterView, LoginView

# urlpatterns = [
#     path('upload/', upload_image,include('rest_framework.urls'), name='upload-image'),
#     path('list/',include('rest_framework.urls'), list_images, name='list-images'),
# ]

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import upload_image, list_images

urlpatterns = [
    path('upload-image/', upload_image, name='upload-image'),
    path('list-image/', list_images, name='list-images'),
    path('upload-video/', upload_video, name='upload-video'),
    path('list-videos/', list_videos, name='list-videos'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]

urlpatterns = format_suffix_patterns(urlpatterns)