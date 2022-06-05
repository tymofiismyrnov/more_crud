from django.db import models
from django.urls import reverse


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})


class Contractor(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('contractor-detail', kwargs={'pk': self.pk})
