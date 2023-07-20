from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(default=10)
    father_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=10)


    def __str__(self):
        return self.name

class Category(models.Model):
    category_name = models.CharField(max_length=120, verbose_name="Category Name")
    
    def __str__(self):
        return self.category_name

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

