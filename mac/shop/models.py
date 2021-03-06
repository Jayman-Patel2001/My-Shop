from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length = 50)
    category = models.CharField(max_length=50 , default="")
    subcategory = models.CharField(max_length=50 , default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length = 200)
    publish_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default = "")


    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=30, default="")
    phone = models.CharField(max_length=10, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return 'Message from' + self.name + '-' + self.email

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=499)
    amount = models.IntegerField(default = 0)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    phone = models.CharField(max_length=10 , default="")
    zip_code = models.CharField(max_length=50)

    def __str__(self):
        return 'Order from ' + self.name + '-' + self.email

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    email = models.CharField(max_length=60 , default="")
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

    def __str__(self):
        return 'Order Update of email- ' + self.email
        
def __str__(self):
    return self.update_desc[0:7] + "..."