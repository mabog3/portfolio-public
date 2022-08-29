from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

# https://citizix.com/how-to-store-django-static-and-media-files-in-amazon-s3/

class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
    #default_acl = 'public-read'

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
    file_overwrite = False
    #default_acl = 'public-read'