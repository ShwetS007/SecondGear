from django.db import models

class Cars(models.Model):
    # Existing fields
    model_name = models.CharField(max_length=30)
    car_type = models.CharField(max_length=30)  # Consider renaming to `car_type` (typo fix)
    km_run = models.IntegerField()
    mfg_year = models.IntegerField()  # Changed to IntegerField for storing just the year
    car_img = models.ImageField(upload_to='img/', null=True, blank=True)
    no_of_seats = models.IntegerField()  # Typo fix from `no_of_seets`
    engine_type = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price as decimal for currency
    contact = models.CharField(max_length=15)  # Phone numbers can include country codes, so CharField

    # Suggested new fields
    transmission = models.CharField(max_length=15, choices=[('Automatic', 'Automatic'), ('Manual', 'Manual')])
    fuel_type = models.CharField(max_length=15, choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')])
    color = models.CharField(max_length=20)
    registration_state = models.CharField(max_length=30)  # State where the car is registered
    owner_count = models.IntegerField(help_text="Number of previous owners")
    insurance_validity = models.DateField(null=True, blank=True, help_text="Expiry date of insurance")
    last_service_date = models.DateField(null=True, blank=True, help_text="Last service date")
    description = models.TextField(null=True, blank=True, help_text="Additional details about the car condition, features, etc.")
    is_featured = models.BooleanField(default=False, help_text="Mark if this is a featured listing")
    is_sold = models.BooleanField(default=False, help_text="Mark if the car is sold")

    def __str__(self):
        return f"{self.model_name} ({self.mfg_year})"
