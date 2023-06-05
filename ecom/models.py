from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name

class Categorie(models.Model):
    nom_Cat=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self) :
        return self.nom_Cat

class Product(models.Model):
    name=models.CharField(max_length=80)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    price = models.FloatField()
    description=models.TextField()
    categorie=models.ForeignKey(Categorie,on_delete=CASCADE)

    def __str__(self):
        return self.name


class Orders(models.Model):
    STATUS =(
        ('En attente','En attente'),
        ('Confirmée','Confirmée'),
        ('En cours de livraison','En cours de livraison'),
        ('Livrée','Livrée'),
    )
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)






