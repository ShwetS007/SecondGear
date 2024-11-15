from django import forms
from .models import Cars

class CarForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = [
            'model_name', 'car_type', 'km_run', 'mfg_year', 'car_img', 'no_of_seats', 'engine_type', 'price', 
            'contact', 'transmission', 'fuel_type', 'color', 'registration_state', 'owner_count', 
            'insurance_validity', 'last_service_date', 'description', 'is_featured', 'is_sold'
        ]
        
        # Customizing form field widgets
        widgets = {
            'mfg_year': forms.NumberInput(attrs={'placeholder': 'e.g., 2020', 'min': 1900, 'max': 2024}),
            'insurance_validity': forms.DateInput(attrs={'type': 'date'}),
            'last_service_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Add details about the car\'s condition, features, etc.'}),
            'transmission': forms.Select(choices=[('Automatic', 'Automatic'), ('Manual', 'Manual')]),
            'fuel_type': forms.Select(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')]),
        }

    # Custom validation
    def clean_km_run(self):
        km_run = self.cleaned_data.get('km_run')
        if km_run < 0:
            raise forms.ValidationError("Kilometers run cannot be negative.")
        return km_run

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price

    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        if len(str(contact)) < 10:
            raise forms.ValidationError("Contact number must be at least 10 digits.")
        return contact
