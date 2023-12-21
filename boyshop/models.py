from django.db import models



class Post(models.Model):
    nomi = models.CharField(max_length=255)
    text = models.TextField(max_length=1000)


    def __str__(self):
        return self.nomi
    

    



