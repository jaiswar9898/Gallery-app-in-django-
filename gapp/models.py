from django.db import models

# Create your models here.
from django.db import models
from django.shortcuts import reverse

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.
import datetime
class Blog(models.Model):
    
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    Img = models.ImageField(upload_to='images/',blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.user_id)

       
   