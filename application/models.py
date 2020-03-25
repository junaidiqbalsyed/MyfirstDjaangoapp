from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=500 , )
    phone =models.IntegerField()
    email = models.CharField(max_length = 100)
    data_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
     
 

class Tag(models.Model):
    name = models.CharField(max_length=500 , )    
    def __str__(self):
        return self.name



class Product(models.Model):
    List = (
        ("Indoor","Indoor"),
        ("Out Door","Out Door"),
    )
    name =models.CharField(max_length = 200)
    price = models.FloatField(max_length=10)
    category = models.CharField(max_length = 200,choices = List)
    data_created = models.DateTimeField(auto_now_add=True)
    Tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ("Pending","Pending"),
        ("Out for delevaary" , "Out for Delevary"),
        ("Delevered","Delevered"),
    )
    data_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length = 100 , choices = STATUS)
    Customer = models.ForeignKey(Customer,null = True , on_delete=models.SET_NULL)
    Product = models.ForeignKey(Product,null = True , on_delete=models.SET_NULL)

   