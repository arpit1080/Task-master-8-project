from django.db import models

class User (models.Model):
    Picture = models.ImageField(upload_to='images/')
    Name = models.CharField (max_length = 150)
    Age = models.IntegerField ()
    City = models.CharField (max_length = 150)
    Email = models.EmailField ()
    Phone = models.CharField(max_length=10)
    Post = models.CharField(max_length = 150)
    StartDate = models.DateField()



class Meta:
    db_table = 'todolist'