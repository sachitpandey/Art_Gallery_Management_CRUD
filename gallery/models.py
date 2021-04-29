from django.db import models

# Create your models here.
class Art(models.Model):  
    artid = models.IntegerField()  
    artist = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)  
    iscolor = models.BooleanField()  
    artcost = models.FloatField()
    artdate = models.DateField()
    artimg = models.ImageField(upload_to='images/')
    class Meta:  
        db_table = "gallery"  