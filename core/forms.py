from django.forms import ModelForm, Form
from .models import Feature


class FeatureForm(ModelForm):
    class Meta:
        model = Feature
        fields = [
            "name",         
            "description",
        ]
