from django.db import models 
from django.contrib.auth.models import User
import uuid

# User specific collection model having title, description and list of movies
class Collections(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="collection", related_query_name="collection")
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    movies = models.JSONField()

    def set_user(self, user):
        self.user = user
        self.save()
    
    def get_id(self):
        return self.uuid
