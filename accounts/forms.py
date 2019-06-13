from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        """
        Check if user exist and then authenticate password"""

        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        if not email or not password:
            return super().clean()
        user = User.objects.filter(email=email).first()
        if not user:
            raise forms.ValidationError("wrong email")
        self.user = authenticate(username=user.username, password=password)
        if self.user is None:
            raise forms.ValidationError("wrong email or password")
        return super().clean()


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password")

    def save(self, commit=True):
        """
        add username and password before saving user
        """
        user = super().save(commit=False)
        if commit:
            username = f"{user.first_name}_{user.last_name}"
            count = User.objects.filter(username=username).count()
            if count > 0:
                username = username + "_" + str(count + 1)
            user.username = username
            user.set_password(user.password)
            user.save()
        return user

    def clean_email(self):
        """Check if user already registered"""

        email = self.cleaned_data.get("email")
        if not email:
            return email
        user_qs = User.objects.filter(email=email)
        if user_qs:
            raise forms.ValidationError("email already exist")
        return email

