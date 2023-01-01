from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    terms_accepted_at = models.DateTimeField(blank=True, null=True)
    marketing_list_accepted_at = models.DateTimeField(blank=True, null=True)
    avatar = models.ImageField(null=True, upload_to="avatars/")

    @property
    def marketing_list_accepted(self) -> bool:
        return bool(self.marketing_list_accepted_at)

    def __str__(self):
        return self.email


class UserFeedback(BaseModel):
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    text = models.TextField()

    def __str__(self):
        return self.text
