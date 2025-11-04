from django import forms
from .models import PortfolioItem

class PortfolioItemForm(forms.ModelForm):
    
    class Meta:
        model = PortfolioItem
        fields = ['coin_id', 'amount']
        
        widgets = {
            'coin_id': forms.TextInput(attrs={'placeholder': 'e.g., bitcoin'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'e.g., 0.5'}),
        }