from django.db import models

# Create your models here.


status = (
    (0, 'inactive'),
    (1, 'active'),
)

# Create your models here.

class Poll(models.Model):
    title = models.CharField(max_length= 200 )
    question = models.CharField(max_length= 200)
    active_untill = models.DateTimeField()
    status = models.IntegerField(default= 0, choices= status)

class Option(models.Model):
    title = models.CharField(max_length= 200)

class Response(models.Model):
    name = models.CharField(max_length= 100)
    response_time = models.DateTimeField()

# Create your models here.



class Poll(models.Model):
    title = models.CharField(max_length=200)
    question = models.CharField(max_length=200)  
    active_until = models.DateTimeField()
    status = models.IntegerField(choices=[
        (0, 'Inactive'),
        (1, 'Active'),
        (2, 'Closed'),
    ])

    def __str__(self):
        return self.title  

class Option(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Response(models.Model):
    name = models.CharField(max_length=100)  
    response_time = models.DateTimeField()

    def __str__(self):
        return self.name
 
