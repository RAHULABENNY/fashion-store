from django import forms
from .models import Category,Clothitems


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'e.g male,female,kids'})
        }

class ClothItemsForm(forms.ModelForm):
    class Meta:
        model=Clothitems
        fields=['name','description','price','image','category','is_avilable']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-controlo','rows':3}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
        }



