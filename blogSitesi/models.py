from django.db import models
class Gonderi(models.Model):
    turler = models.CharField(max_length=200)
    icerik = models.TextField()
    def yayinla(self):
        self.save()

    def __str__(self):
        return self.turler



