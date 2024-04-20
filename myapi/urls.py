from django.urls import path,include

from ApiProject import settings
from .views import upload_image, list_images, upload_video, list_videos, RegisterView, LoginView, logout, \
    get_csrf_token, serve_media

# urlpatterns = [
#     path('upload/', upload_image,include('rest_framework.urls'), name='upload-image'),
#     path('list/',include('rest_framework.urls'), list_images, name='list-images'),
# ]

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import upload_image, list_images, serve_media
from django.conf.urls.static import static
urlpatterns = [
    path('upload-image/', upload_image, name='upload-image'),
    path('list-image/', list_images, name='list-images'),
    path('upload-video/', upload_video, name='upload-video'),
    path('list-videos/', list_videos, name='list-videos'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),
    path('media/<path:file_path>/', serve_media, name='serve_media'),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns = format_suffix_patterns(urlpatterns)
