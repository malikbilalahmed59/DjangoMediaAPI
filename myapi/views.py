from rest_framework import status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from .models import Image
from .serializers import ImageSerializer, RegisterSerializer, User
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Video
from .serializers import VideoSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


@api_view(['POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def upload_image(request):
    print(request.COOKIES)
    if request.method == 'POST':
        image_file = request.FILES.get('image')
        if image_file:
            name = request.POST.get('name', '')
            image_instance = Image(user=request.user, name=name, image=image_file)
            image_instance.save()
            serializer = ImageSerializer(image_instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'No image file provided'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Unsupported request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
@api_view(['POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def upload_video(request):
    print(request.COOKIES)
    if request.method == 'POST':
        image_file = request.FILES.get('video')
        if image_file:
            name = request.POST.get('name', '')
            video_instance = Video(user=request.user, name=name, video=image_file)
            video_instance.save()
            serializer = VideoSerializer(video_instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'No image file provided'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Unsupported request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def list_images(request):
    images = Image.objects.filter(user=request.user)
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)


# @api_view(['POST'])
# @csrf_exempt
# @permission_classes([IsAuthenticated])
# def upload_video(request):
#     if request.method == 'POST':
#         video_file = request.FILES.get('video')
#         if video_file:
#             name = request.POST.get('name', '')  # Assuming 'name' is the key in the form data
#             video_instance = Video(user=request.user, name=name, video=video_file)
#             video_instance.save()
#             serializer = VideoSerializer(video_instance)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response({'error': 'No video file provided'}, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response({'error': 'Unsupported request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def list_videos(request):
    videos = Video.objects.filter(user=request.user)
    serializer = VideoSerializer(videos, many=True)
    return Response(serializer.data)


# views.py

# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=email, password=password)
        if user is None:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        token, created = Token.objects.get_or_create(user=user)

        # Update token if it already exists
        if not created:
            token.delete()
            token = Token.objects.create(user=user)

        return Response({'token': token.key})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def logout(request):
    # Retrieve the user's token
    try:
        token = Token.objects.get(user=request.user)
    except Token.DoesNotExist:
        return Response({'detail': 'User does not have a token'}, status=status.HTTP_400_BAD_REQUEST)

    # Delete the user's token
    token.delete()
    return Response({'detail': 'User logged out successfully'}, status=status.HTTP_200_OK)


from django.middleware.csrf import get_token
from django.http import JsonResponse

def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrf_token': token})