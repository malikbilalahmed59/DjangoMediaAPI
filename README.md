# Django Media API

This Django project provides an API for uploading images and videos and retrieving them.

## Setup

1. Clone this repository:
   git clone https://github.com/malikbilalahmed59/DjangoMediaAPI.git

2. Navigate to the project directory:
   cd DjangoMediaAPI

3. Install dependencies:
   pip install -r requirements.txt

4. Run migrations:
   python manage.py migrate

5. Create a superuser (for accessing the admin panel):
   python manage.py createsuperuser

6. Start the development server:
   python manage.py runserver

## Usage

### Uploading Images

To upload an image, send a POST request to the `upload-image/` endpoint with the image file attached as a form data. You can use tools like Postman or cURL for making requests.

Example cURL command:
curl -X POST -F "image=@/path/to/image.jpg" http://localhost:8000/upload-image/

### Retrieving Images

To retrieve all uploaded images, send a GET request to the `list-images/` endpoint.

Example cURL command:
curl http://localhost:8000/list-images/

### Uploading Videos

To upload a video, send a POST request to the `upload-video/` endpoint with the video file attached as a form data.

### Retrieving Videos

To retrieve all uploaded videos, send a GET request to the `list-videos/` endpoint.
