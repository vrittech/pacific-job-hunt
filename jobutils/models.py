from django.db import models

# Create your models here.
class JobLevel(models.Model):
    name = models.CharField(max_length = 200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class JobPosition(models.Model):
    name = models.CharField(max_length = 200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class JobLocation(models.Model):
    name = models.CharField(max_length = 200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class JobTiming(models.Model):
    name = models.CharField(max_length = 200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name