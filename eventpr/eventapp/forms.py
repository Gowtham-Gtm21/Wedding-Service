from django import forms
from.models import *

class DateInput(forms.DateInput):
    input_type='date'

class MakForm(forms.ModelForm):
    class Meta:
        model=Booking_mak
        fields='__all__'
        widgets={
            'Full_Name':forms.TextInput,
            'Phone_Number':forms.NumberInput,
            'Gmail_Address':forms.EmailInput,
            'Event_Name':forms.Select,      
            'Function_Date':DateInput
        }

class DecForm(forms.ModelForm):
    class Meta:
        model=Booking_dec
        fields='__all__'
        widgets={
            'Full_Name':forms.TextInput,
            'Phone_Number':forms.NumberInput,
            'Gmail_Address':forms.EmailInput,
            'Event_Name':forms.Select,      
            'Function_Date':DateInput
        }
       
        
class InvForm(forms.ModelForm):
    class Meta:
        model=Booking_inv
        fields='__all__'
        widgets={
            'Full_Name':forms.TextInput,
            'Phone_Number':forms.NumberInput,
            'Gmail_Address':forms.EmailInput,
            'Event_Name':forms.Select,      
            'Function_Date':DateInput
        }
        
class CatForm(forms.ModelForm):
    class Meta:
        model=Booking_cat
        fields='__all__'
        widgets={
            'Full_Name':forms.TextInput,
            'Phone_Number':forms.NumberInput,
            'Gmail_Address':forms.EmailInput,
            'Event_Name':forms.Select,      
            'Function_Date':DateInput
        }
        
class GifForm(forms.ModelForm):
    class Meta:
        model=Booking_gif
        fields='__all__'
        widgets={
            'Full_Name':forms.TextInput,
            'Phone_Number':forms.NumberInput,
            'Gmail_Address':forms.EmailInput,
            'Event_Name':forms.Select,      
            'Function_Date':DateInput
        }

class WeaForm(forms.ModelForm):
    class Meta:
        model=Booking_wea
        fields='__all__'
        widgets={
            'Full_Name':forms.TextInput,
            'Phone_Number':forms.NumberInput,
            'Gmail_Address':forms.EmailInput,
            'Event_Name':forms.Select,      
            'Function_Date':DateInput
        }

class JewForm(forms.ModelForm):
    class Meta:
        model=Booking_jew
        fields='__all__'
        widgets={
            'Full_Name':forms.TextInput,
            'Phone_Number':forms.NumberInput,
            'Gmail_Address':forms.EmailInput,
            'Event_Name':forms.Select,      
            'Function_Date':DateInput
        }

class VenForm(forms.ModelForm):
    class Meta:
        model=Booking_ven
        fields='__all__'
        widgets={
            'Full_Name':forms.TextInput,
            'Phone_Number':forms.NumberInput,
            'Gmail_Address':forms.EmailInput,
            'Event_Name':forms.Select,      
            'Function_Date':DateInput
        }
        
class ChoForm(forms.ModelForm):
    class Meta:
        model=Booking_cho
        fields='__all__'
        widgets={
            'Full_Name':forms.TextInput,
            'Phone_Number':forms.NumberInput,
            'Gmail_Address':forms.EmailInput,
            'Event_Name':forms.Select,      
            'Function_Date':DateInput
        }
        
class PhoForm(forms.ModelForm):
    class Meta:
        model=Booking_pho
        fields='__all__'
        widgets={
            'Full_Name':forms.TextInput,
            'Phone_Number':forms.NumberInput,
            'Gmail_Address':forms.EmailInput,
            'Event_Name':forms.Select,      
            'Function_Date':DateInput
        }

class MehForm(forms.ModelForm):
    class Meta:
        model=Booking_meh
        fields='__all__'
        widgets={
            'Full_Name':forms.TextInput,
            'Phone_Number':forms.NumberInput,
            'Gmail_Address':forms.EmailInput,
            'Event_Name':forms.Select,      
            'Function_Date':DateInput
        }
        
class DjForm(forms.ModelForm):
    class Meta:
        model=Booking_djs
        fields='__all__'
        widgets={
            'Full_Name':forms.TextInput,
            'Phone_Number':forms.NumberInput,
            'Gmail_Address':forms.EmailInput,
            'Event_Name':forms.Select,      
            'Function_Date':DateInput
        }