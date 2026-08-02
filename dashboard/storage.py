from django.core.files.storage import Storage
from imagekitio import ImageKit
import os


class ImageKitStorage(Storage):

    def __init__(self):
        self.imagekit = ImageKit(
            private_key=os.environ.get("IMAGEKIT_PRIVATE_KEY"),
            public_key=os.environ.get("IMAGEKIT_PUBLIC_KEY"),
            url_endpoint="https://ik.imagekit.io/tafdvsgwf"
        )

    def save(self, name, content, max_length=None):
        response = self.imagekit.upload_file(
            file=content,
            file_name=name
        )

        return response.response_metadata.raw["url"]