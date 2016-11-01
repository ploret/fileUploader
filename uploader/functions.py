import os.path
from django.conf import settings


def handle_uploaded_file(f):
    """ Handle file upload """
    with open(settings.MEDIA_ROOT.replace('\\', '/') + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)