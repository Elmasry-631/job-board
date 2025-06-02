from django import forms

from .models import Apply, Job  # Adjust the import if your model is named differently


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ["name", "email", "website", "resume", "cover_letter"]


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields ="__all__"
        exclude = ["slug", "created_at", "updated_at", "owner"]  # Exclude fields that should not be set by the user