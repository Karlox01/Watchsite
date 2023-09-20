from django import forms    
from .models import ConversationMessage



class ConversationMessageForm(forms.ModelForm):
    is_offer = forms.BooleanField(
        required=False,
        widget=forms.HiddenInput,  # Use a hidden input field
        initial=False,  # Default to False (not an offer)
    )
    class Meta:
        model = ConversationMessage
        fields = ['content', 'is_offer']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }