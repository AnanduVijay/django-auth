from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

User = get_user_model()

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Confirm password"), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            "first_name", "last_name", "email", "phone_no"
        ]

    def clean_password(self):

        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 and password2 and password1 != password2:
            raise ValueError(_("Password donot match !!"))
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    email = forms.EmailField(label=_("email"))
    password = forms.CharField(label=_("password"), widget=forms.PasswordInput)


