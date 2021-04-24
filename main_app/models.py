from django.db import models
from django.urls import reverse

class Food(models.Model):
    name = models.CharField(max_length=50)
    # Other goodness such as 'def __str__():' below
    def __str__(self):
        return f'{self.name}'

    # Add this method
    def get_absolute_url(self):
        return reverse('food_detail', kwargs={'food_id': self.id})    
        class Meta:
            ordering = ['-date']

class Wine(models.Model):
    name = models.CharField(max_length=100)
    winetype = models.CharField(max_length=100)
    cost = models.IntegerField()
    foods = models.ManyToManyField(Food)

    def __str__(self):
        return self.name

# Create your models here.
    def get_absolute_url(self):
        return reverse('detail', kwargs={'wine_id': self.id})

class Year(models.Model):
    year = models.IntegerField()
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)


def get_absolute_url(self):
    return reverse('detail', kwargs={'wine_id': self.id})


class Photo(models.Model):
    url = models.CharField(max_length=200)
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for wine_id: {self.wine_id} @{self.url}"