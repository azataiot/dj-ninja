from django.db import models
from django.contrib.auth import get_user_model
import uuid


# Create your models here.


class One(models.Model):
    uid = models.UUIDField(
        default=uuid.uuid4,
        editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    slug = models.SlugField(max_length=16, help_text="Slug of One, (ASCII only)")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'One'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "One: " + str(self.uid)


class Two(models.Model):
    uid = models.UUIDField(
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=200, help_text="Name of Two")
    default = models.ForeignKey(One, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Two'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "Two: " + str(self.uid)
