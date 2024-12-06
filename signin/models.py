from django.db import models

class BesantUser(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=8)  # For hashed passwords

    def __str__(self):
        return self.username