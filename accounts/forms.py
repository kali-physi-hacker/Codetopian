from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class UserCreationForm(forms.ModelForm):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=255, required=True)
    password1 = forms.CharField(required=True, strip=False)
    password2 = forms.CharField(required=True, strip=False)

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "full_name")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "Password mismatch"
            )
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password1"))
        if commit:
            user.save()
        return user
