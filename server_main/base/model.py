
from django.db import models


class BaseModel(models.Model):
    """
    Base model for all models in this project
    have created_at and updated_at
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True