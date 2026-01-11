from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
# from accounts.models import UserProfile  # Removed: accounts app deleted
from .models import Product, Category, Supplier, StockMovement



class ProductForm(forms.ModelForm):
    """Enhanced product form with better styling"""
    
    class Meta:
        model = Product
        fields = [
            'name', 'description', 'category', 'supplier', 'sku', 'barcode',
            'cost_price', 'selling_price', 'stock_quantity', 'minimum_stock',
            'image', 'is_active'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter product description'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'supplier': forms.Select(attrs={
                'class': 'form-control'
            }),
            'sku': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Auto-generated if left blank'
            }),
            'barcode': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter barcode (optional)'
            }),
            'cost_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
            'selling_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
            'stock_quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),
            'minimum_stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }

class CategoryForm(forms.ModelForm):
    """Form for category management"""
    
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter category description'
            })
        }

class SupplierForm(forms.ModelForm):
    """Form for supplier management"""
    
    class Meta:
        model = Supplier
        fields = ['name', 'contact_person', 'email', 'phone', 'address']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter supplier name'
            }),
            'contact_person': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter contact person name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter supplier address'
            })
        }

class StockMovementForm(forms.ModelForm):
    """Form for stock movement management"""
    
    class Meta:
        model = StockMovement
        fields = ['product', 'movement_type', 'quantity', 'reason', 'reference']
        widgets = {
            'product': forms.Select(attrs={
                'class': 'form-control'
            }),
            'movement_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1'
            }),
            'reason': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter reason for stock movement'
            }),
            'reference': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter reference number (optional)'
            })
        }