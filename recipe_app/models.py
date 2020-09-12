#[V1/2]import models as part of setup
from django.db import models
#[Auth] imported User to implement OneToOneField
from django.contrib.auth.models import User

# Create your models here.
#[V1/2] Added Author & Recipe Models
#[Auth] added User field in Author Model to implement Author OneToOne functionality
class Author(models.Model):
    name = models.CharField(max_length=80)
    bio = models.TextField(max_length=80)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField('Recipe', related_name='favorite', symmetrical=False, blank=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=30)
    instructions = models.TextField(max_length=60)

    def __str__(self):
        return self.title
