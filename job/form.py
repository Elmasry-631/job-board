from django import forms

from .models import Apply  # Adjust the import if your model is named differently

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = [
            'name',
            'email',
            'website',
            'resume',
            'cover_letter'
        ]