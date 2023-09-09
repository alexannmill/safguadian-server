from django.db import models


class SafeConsumptionSite(models.Model):
    facility = models.CharField(max_length=120)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=10)
    open_hour = models.TimeField(auto_now_add=False,  auto_created=False)
    close_hour = models.TimeField(auto_now_add=False,  auto_created=False)

    # def _str_(self):
    #     return self.facility
class Foodbank(models.Model):
    facility = models.CharField(max_length=120)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=10)
    open_hour = models.TimeField(auto_now_add=False,  auto_created=False)
    close_hour = models.TimeField(auto_now_add=False,  auto_created=False)

    # def _str_(self):
    #     return self.facility

class DrugTesting(models.Model):
    facility = models.CharField(max_length=120)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=10)
    open_hour = models.TimeField(auto_now_add=False,  auto_created=False)
    close_hour = models.TimeField(auto_now_add=False,  auto_created=False)

    # def _str_(self):
    #     return self.facility

class DetoxCentre(models.Model):
    facility = models.CharField(max_length=120)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=10)
    open_hour = models.TimeField(auto_now_add=False,  auto_created=False)
    close_hour = models.TimeField(auto_now_add=False,  auto_created=False)

    # def _str_(self):
    #     return self.facility

class Shelters(models.Model):
    facility = models.CharField(max_length=120)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=10)
    open_hour = models.TimeField(auto_now_add=False,  auto_created=False)
    close_hour = models.TimeField(auto_now_add=False,  auto_created=False)
    charts_allowed = models.BooleanField(default=False)
    meals = models.BooleanField(default=False)
    pets_allowed = models.BooleanField(default=False)
    category = models.BooleanField(default=False) 

    # def _str_(self):
    #     return self.facility

class AllowedCamping(models.Model):
    facility = models.CharField(max_length=120)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=10)
    open_hour = models.TimeField(auto_now_add=False,  auto_created=False)
    close_hour = models.TimeField(auto_now_add=False,  auto_created=False)

    # def _str_(self):
    #     return self.facility

class Pharmacy(models.Model):
    facility = models.CharField(max_length=120)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=10)
    open_hour = models.TimeField(auto_now_add=False,  auto_created=False)
    close_hour = models.TimeField(auto_now_add=False,  auto_created=False)

    # def _str_(self):
    #     return self.facility
class Hospitals(models.Model):
    facility = models.CharField(max_length=120)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=10)

    # def _str_(self):
    #     return self.facility