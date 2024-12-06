from django import forms
from django.contrib.auth.models import User
from .models import Member
from django.core.validators import MinValueValidator

class ExpenseForm(forms.Form):
    heading = forms.CharField(max_length=100, required=True)
    amount = forms.IntegerField(required=True,validators=[MinValueValidator(1)])

    def __init__(self, *args, **kwargs):
        self.balance_amount = kwargs.pop('balance_amount', None)
        super().__init__(*args, **kwargs)

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount > self.balance_amount:
            raise forms.ValidationError("Insufficient balance.")
        return amount

class MembersForm(forms.Form):
    email_id = forms.EmailField(required=True)
    contribution = forms.IntegerField(required=True, min_value=0)

    def __init__(self, *args, **kwargs):
        self.event_id = kwargs.pop('event_id', None)
        super().__init__(*args, **kwargs)
 
    def clean_email_id(self):
        email_id = self.cleaned_data.get('email_id')
        email_id = email_id.lower()
        try:
            user = User.objects.get(email=email_id)
        except User.DoesNotExist:
            raise forms.ValidationError("User does not exist.")
        
        if user.members.filter(event__id=self.event_id).exists():
            raise forms.ValidationError("User is already a member of this event.")
        
        return email_id
