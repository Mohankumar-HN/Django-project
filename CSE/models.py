

# Create your models here.
from pyexpat import model


class Sudent(models.Model):
    name = model.CharField(max_length=30)
    departent = models.CharField(max_length=10)
    rollnumber = models.IntegerField()
    def _str_(self):
        return self.name 