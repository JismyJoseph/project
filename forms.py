from django import forms
from quizapp.models import registration
class registrationForm(forms.ModelForm):
    class Meta:
        model=registration
        fields='__all__'
