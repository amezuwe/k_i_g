from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)



class ProfileForm(forms.ModelForm):
    # first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # investment_goal = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Profile 
        fields = ['first_name', 'last_name', 'email', 'phone', 'investment_goal']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['investment_goal'].widget.attrs.update({'class': 'form-control'})
        # self.fields['comment'].widget.attrs.update(size='40')
        