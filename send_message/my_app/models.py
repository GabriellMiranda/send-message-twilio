from django.db import models

class Upload(models.Model):
    whatsapp_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.whatsapp_number