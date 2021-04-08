from django.forms import ModelForm
from .models import journalEntry

class EntryForm(ModelForm):
    class Meta:
        model = journalEntry
        fields = ('text', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class' : 'textarea', 'placeholder' : 'What\'s on your mind?'})