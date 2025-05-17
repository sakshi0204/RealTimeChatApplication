from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
        required=True
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'college_id', 'role']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your Username'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter your Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your Email Address'}),
            'college_id': forms.TextInput(attrs={'placeholder': 'Enter your College ID'}),
            'role': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for field in ['username', 'name', 'email', 'college_id', 'role', 'password1', 'password2']:
            self.fields[field].required = True

        for field in self.fields.values():
            field.widget.attrs.update({
                'style': 'text-align:center; background-color:#dadee1; border:none; padding:0.5rem 1rem; border-radius:2rem; margin-bottom:1rem; width:100%;'
            })

    def clean_college_id(self):
        college_id = self.cleaned_data.get('college_id', '').strip()

        if not college_id:
            raise forms.ValidationError("College ID is required.")

        if User.objects.filter(college_id=college_id).exists():
            raise forms.ValidationError("This College ID is already registered!")

        return college_id

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            raise forms.ValidationError("Email is required.")
        
        return email
