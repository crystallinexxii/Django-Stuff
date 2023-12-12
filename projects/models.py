from django.db import models

# Create your models here.


class Project (models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='images/',null=True, blank=True)
    slug = models.SlugField(max_length=100,blank='',null=False)
    link= models.CharField(max_length=200,blank='',null=False)

    main_branch = models.CharField(max_length=10,default='master')


    def __str__(self):
        return self.title