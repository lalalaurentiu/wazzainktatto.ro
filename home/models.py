from django.db import models

class portofoliu(models.Model):
    image = models.ImageField(upload_to = "portofoliu/pages")

    def __str__(self):
        return self.image.name

class ClientRezervation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone =  models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    duration = models.TimeField(null=True ,blank=True)
    description = models.TextField(null=True ,blank=True)
    image = models.ImageField(upload_to = "clients/images", null=True, blank=True)
    anounced = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class AdminVacantion(models.Model):
    to_date = models.DateField()
    at_date = models.DateField()

    def __str__(self):
        return f"Vacantion to {self.to_date} at {self.at_date}"



    