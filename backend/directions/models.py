from django.db import models

class Direction(models.Model):
    city = models.CharField(blank=False, null=False, max_length=20)
    photo = models.ImageField(upload_to="directions", blank=True, null=True, verbose_name='Фотография')
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.city
    
class PopularPlace(models.Model):
    title = models.CharField(blank=False, null=False, max_length=20)
    photo = models.ImageField(upload_to="places", blank=True, null=True, verbose_name='Фотография')
    description = models.TextField(blank=True, null=True)
    city = models.ForeignKey(Direction, on_delete=models.CASCADE, blank=False)
    
    def __str__(self):
        return self.title