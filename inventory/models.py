from django.db import models

# Create your models here.


class Vehicle(models.Model):
    CATEGORY_CHOICES = [
        ('SUV', 'SUV'),
        ('Sedan', 'Sedan'),
        ('Wagon', 'Wagon'),
        ('Pickup', 'Pickup'),
    ]
    
    TRANSMISSION_CHOICES=[
        ('Automatic','Automatic'),
        ('Manual','Manual'),
        ('CVT','CVT'),]
    
    FUEL_CHOICES=[
        ('Petrol','Petrol'),
        ('Diesel','Diesel'),
        ('Electric','Electric'),
        ('Hybrid','Hybrid'),
    ]
    
    drive_type_choices=[
        ('4WD','4WD'),
        ('RWD','RWD'),
        ('AWD','AWD'),
    ]

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='vehicles/')
    available = models.BooleanField(default=True)
    engine_size = models.CharField(max_length=50, null=True, blank=True)
    transmission = models.CharField(max_length=50, choices=TRANSMISSION_CHOICES, null=True, blank=True)
    fuel_type = models.CharField(max_length=30, choices=FUEL_CHOICES,null=True, blank=True)
    drive_type = models.CharField(max_length=30 , choices=drive_type_choices, null=True, blank=True)
    mileage = models.PositiveIntegerField(null=True, blank=True)
    registration_year = models.PositiveIntegerField(null=True, blank=True)
    ownership_history = models.CharField(max_length=100, null=True, blank=True)
    logbook_available = models.BooleanField(default=False)
    insurance_valid = models.BooleanField(default=False)
    color = models.CharField(max_length=30, null=True, blank=True)
    seating_capacity = models.PositiveIntegerField(null=True, blank=True)
    interior_material = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title
    
    
class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='vehicles/gallery/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.vehicle.title}"
