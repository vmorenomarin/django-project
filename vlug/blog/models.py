"Models for Blog project"

from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    "Post model class"
    class Status(models.TextChoices):
        "Status for Post model"
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )

    class Meta():
        '''
        Define metadata para el modelo. 

        En el valor para 'ordering', retornará en 
        orden en el que se retornarán los registros
        de la BD. El guión indica que se retornará enorden descentende por el campo publish
        '''
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    # def __str__(self):
    #     return self.title
