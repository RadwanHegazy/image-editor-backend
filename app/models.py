from django.db import models
from uuid import uuid4


class ImageModel (models.Model) : 
    id = models.UUIDField(default=uuid4,primary_key=True,editable=False)
    image = models.ImageField(upload_to="original-images/")
    upload_at = models.DateTimeField(auto_now_add=True)