from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
import datetime

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, null=True)
    email = models.EmailField(max_length=127, null=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='uploads/videos/',
                             validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    thumbnail = models.FileField(default="uploads/thumbnails/thumbnail-default.jpg",
                                 upload_to='uploadsthumbnails/',
                                 validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    description = models.TextField(blank=True)
    duration = models.DurationField()
    date_posted = models.DateTimeField(auto_now_add=True)
    takedown_performed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Takedown(models.Model):
    COPYRIGHT = "Copyright"
    ABUSIVE = "Abusive"
    ILLEGAL = "Illegal"
    TYPE_CHOICES = (
        (COPYRIGHT, "Copyright"),
        (ABUSIVE, "Abusive"),
        (ILLEGAL, "Illegal"),
    )
    video = models.ForeignKey(Video, null=True, on_delete=models.SET_NULL)
    uploader = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)
    takedown_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    comments = models.CharField(max_length=255, null=True, default=None,
                                        db_comment="A message about the reason for the takedown, such as copyright "
                                                   "infringement or abusive nature or illegal content")

class Track(models.Model):
    isrc = models.CharField(max_length=12, unique=True, null=True)
    upc = models.CharField(max_length=12, unique=True, null=True)
    ean = models.CharField(max_length=13, unique=True, null=True)
    title = models.CharField(max_length=255, null=True, default=None)
    duration: models.DurationField(default=datetime.timedelta())
    publisher = models.CharField(max_length=255, null=True, default=None)
    artist = models.CharField(max_length=255, null=True, default=None)
    purchase_url = models.URLField(null=True, default=None)

    def __str__(self):
        return self.title
