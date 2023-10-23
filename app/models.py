from django.db import models


class Boat(models.Model):
    # id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    length = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Slip(models.Model):
    number = models.PositiveIntegerField()
    current_boat = models.PositiveIntegerField(blank = True, null = True)

    def __str__(self):
        return self.number + ", " + self.current_boat
    
    





