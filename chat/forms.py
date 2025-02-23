from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    """Form for users to input chat messages."""
    class Meta:
        model = Message
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Type your message here...'
            })
        }
