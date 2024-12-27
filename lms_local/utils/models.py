import uuid
from colorhash import ColorHash
from django.db import models


class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def hex_color(self):
        return ColorHash(self.uuid).hex

    class Meta:
        abstract = True
