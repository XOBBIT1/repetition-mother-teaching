from django.db import models


class Post(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    title = models.CharField("Название", max_length=256, unique=False, blank=False, null=False)
    text = models.TextField("Описание", blank=False, null=False)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title