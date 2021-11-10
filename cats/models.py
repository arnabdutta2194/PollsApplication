from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Breed(models.Model):
    name = models.CharField(
            max_length=200,
            help_text="Enter an item",
            validators= [MinLengthValidator(2,"Name must be greater than 1 character")]
    )

    def __str__(self):
        return self.name

class Cats(models.Model):
    nickname = models.CharField(
            max_length=200,
            validators= [MinLengthValidator(2,"Nickname must be greater than 1 character")]
    )
    weight = models.FloatField()
    foods = models.CharField(
            max_length=200,
            validators= [MinLengthValidator(2,"Foods must be greater than 1 character")]
    )
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.nickname
