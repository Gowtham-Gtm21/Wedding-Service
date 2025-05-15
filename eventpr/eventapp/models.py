from django.db import models

# Create your models here.
class Makeup(models.Model):
    img=models.ImageField(upload_to="mak")
    name=models.CharField(max_length=50)
    rate=models.CharField(max_length=50)
    review=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Decorator(models.Model):
    img=models.ImageField(upload_to="dec")
    name=models.CharField(max_length=50)
    rate=models.CharField(max_length=50)
    review=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Invitation(models.Model):
    img=models.ImageField(upload_to="inv")
    name=models.CharField(max_length=50)
    rate=models.CharField(max_length=50)
    review=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Catering(models.Model):
    img=models.ImageField(upload_to="cat")
    name=models.CharField(max_length=50)
    rate=models.CharField(max_length=50)
    review=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Gift(models.Model):
    img=models.ImageField(upload_to="gif")
    name=models.CharField(max_length=50)
    rate=models.CharField(max_length=50)
    review=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Wear(models.Model):
    img=models.ImageField(upload_to="wea")
    name=models.CharField(max_length=50)
    rate=models.CharField(max_length=50)
    review=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Jewellery(models.Model):
    img=models.ImageField(upload_to="jew")
    name=models.CharField(max_length=50)
    rate=models.CharField(max_length=50)
    review=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Photographer(models.Model):
    img=models.ImageField(upload_to="pho")
    name=models.CharField(max_length=50)
    rate=models.CharField(max_length=50)
    review=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Hotel(models.Model):
    img=models.ImageField(upload_to="ven")
    name=models.CharField(max_length=50)
    rate=models.CharField(max_length=50)
    review=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Choreographer(models.Model):
    img=models.ImageField(upload_to="cho")
    name=models.CharField(max_length=50)
    rate=models.CharField(max_length=50)
    review=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Mehendi(models.Model):
    img=models.ImageField(upload_to="meh")
    name=models.CharField(max_length=50)
    rate=models.CharField(max_length=50)
    review=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Dj(models.Model):
    img=models.ImageField(upload_to="djs")
    name=models.CharField(max_length=50)
    rate=models.CharField(max_length=50)
    review=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Booking_mak(models.Model):
    Full_Name=models.CharField(max_length=50)
    Phone_Number=models.CharField(max_length=50)
    Gmail_Address=models.CharField(max_length=50)
    Event_Name=models.ForeignKey(Makeup,on_delete=models.CASCADE)
    Function_Date=models.DateField()
    date_on=models.DateField(auto_now=True)

class Booking_dec(models.Model):
    Full_Name=models.CharField(max_length=50)
    Phone_Number=models.CharField(max_length=50)
    Gmail_Address=models.CharField(max_length=50)
    Event_Name=models.ForeignKey(Decorator,on_delete=models.CASCADE)
    Function_Date=models.DateField()
    date_on=models.DateField(auto_now=True)

class Booking_inv(models.Model):
    Full_Name=models.CharField(max_length=50)
    Phone_Number=models.CharField(max_length=50)
    Gmail_Address=models.CharField(max_length=50)
    Event_Name=models.ForeignKey(Invitation,on_delete=models.CASCADE)
    Function_Date=models.DateField()
    date_on=models.DateField(auto_now=True)
    
class Booking_cat(models.Model):
    Full_Name=models.CharField(max_length=50)
    Phone_Number=models.CharField(max_length=50)
    Gmail_Address=models.CharField(max_length=50)
    Event_Name=models.ForeignKey(Catering,on_delete=models.CASCADE)
    Function_Date=models.DateField()
    date_on=models.DateField(auto_now=True)
    
class Booking_gif(models.Model):
    Full_Name=models.CharField(max_length=50)
    Phone_Number=models.CharField(max_length=50)
    Gmail_Address=models.CharField(max_length=50)
    Event_Name=models.ForeignKey(Gift,on_delete=models.CASCADE)
    Function_Date=models.DateField()
    date_on=models.DateField(auto_now=True)

class Booking_wea(models.Model):
    Full_Name=models.CharField(max_length=50)
    Phone_Number=models.CharField(max_length=50)
    Gmail_Address=models.CharField(max_length=50)
    Event_Name=models.ForeignKey(Wear,on_delete=models.CASCADE)
    Function_Date=models.DateField()
    date_on=models.DateField(auto_now=True)
    
class Booking_jew(models.Model):
    Full_Name=models.CharField(max_length=50)
    Phone_Number=models.CharField(max_length=50)
    Gmail_Address=models.CharField(max_length=50)
    Event_Name=models.ForeignKey(Jewellery,on_delete=models.CASCADE)
    Function_Date=models.DateField()
    date_on=models.DateField(auto_now=True)
    
class Booking_pho(models.Model):
    Full_Name=models.CharField(max_length=50)
    Phone_Number=models.CharField(max_length=50)
    Gmail_Address=models.CharField(max_length=50)
    Event_Name=models.ForeignKey(Photographer,on_delete=models.CASCADE)
    Function_Date=models.DateField()
    date_on=models.DateField(auto_now=True)
    
class Booking_ven(models.Model):
    Full_Name=models.CharField(max_length=50)
    Phone_Number=models.CharField(max_length=50)
    Gmail_Address=models.CharField(max_length=50)
    Event_Name=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    Function_Date=models.DateField()
    date_on=models.DateField(auto_now=True)
    
class Booking_cho(models.Model):
    Full_Name=models.CharField(max_length=50)
    Phone_Number=models.CharField(max_length=50)
    Gmail_Address=models.CharField(max_length=50)
    Event_Name=models.ForeignKey(Choreographer,on_delete=models.CASCADE)
    Function_Date=models.DateField()
    date_on=models.DateField(auto_now=True)
    
class Booking_meh(models.Model):
    Full_Name=models.CharField(max_length=50)
    Phone_Number=models.CharField(max_length=50)
    Gmail_Address=models.CharField(max_length=50)
    Event_Name=models.ForeignKey(Mehendi,on_delete=models.CASCADE)
    Function_Date=models.DateField()
    date_on=models.DateField(auto_now=True)

class Booking_djs(models.Model):
    Full_Name=models.CharField(max_length=50)
    Phone_Number=models.CharField(max_length=50)
    Gmail_Address=models.CharField(max_length=50)
    Event_Name=models.ForeignKey(Dj,on_delete=models.CASCADE)
    Function_Date=models.DateField()
    date_on=models.DateField(auto_now=True)