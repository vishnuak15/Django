from django import forms

from .models import Program,Entity,UserProfileInfo


class ProgramForm(forms.ModelForm):

    class Meta:
        model = Program 
        fields = ('programe_name','no_of_people','place','description')

        widgets = {
            'programe_name': forms.TextInput(attrs={'class': 'textinputclass'}),
            'no_of_people': forms.TextInput(attrs={'class': 'textinputclass'}),
            'place': forms.TextInput(attrs={'class': 'textinputclass'}),
            'programe_name': forms.TextInput(attrs={'class': 'textinputclass'}),
            'description': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
        
class UserForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = UserProfileInfo
        fields = ('name','email','password')
