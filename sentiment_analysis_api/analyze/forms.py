from django.forms import ModelForm
from django import forms
from .models import Analysis


# Model Form for the model 'Analysis' 
class AnalysisForm(ModelForm):
    class Meta:
        model = Analysis
        fields = ['text']
        
        labels = {
            'text': 'Text you want to analyze'
        }

    def __init__(self, *args, **kwargs):
        super(AnalysisForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        