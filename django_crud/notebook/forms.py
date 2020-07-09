from django import forms
from .models import Notebook


class NotebookForm(forms.ModelForm):

    class Meta:

        model = Notebook
        fields = [
            'note_data',
            'draft_user',
            'created_at',
            'updated_at'
        ]