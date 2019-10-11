from django import forms
from .models import Hotel

class HotelForm(forms.ModelForm):
    class Meta:
        # model is our database and fields are our data of the database
        model = Hotel
        fields = '__all__'