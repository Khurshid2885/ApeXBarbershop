from django import forms
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from accounts.models import Code
from accounts.models import CustomUser


class RegisterForm(forms.ModelForm):
    re_password = forms.CharField(max_length=10, widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email", "phone_number", "profile_photo", "password"]

    def save(self, commit=True):
        user = super().save(commit=False)

        cleaned_data = self.cleaned_data
        password = cleaned_data.get("password")
        re_password = cleaned_data.get("re_password")
        image = cleaned_data.get("profile_photo")

        if password or re_password and password == re_password:
            user.set_password(password)

        if image:
            user.profile_photo = image

        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10)

    def custom_login(self, request):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            if user.is_superuser:
                return redirect("services:dashboard")
            elif user.groups.filter(name="barber").exists():
                return redirect("services:barbers_homepage")
            else:
                return redirect("services:home")
        else:
            self.add_error(None, "Invalid username or password")

        return user


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput())

    def clean(self):
        cleaned_data = super().clean()
        user = CustomUser.objects.filter(email=cleaned_data.get("email")).first()

        if not user:
            self.add_error("email", "The email does not exist")
        else:
            # Store in cleaned_data dict if you keep encountering CustomUser object does not have get method ERROR.
            cleaned_data["user"] = user
        return cleaned_data


class VerifyCodeForm(forms.Form):
    code = forms.CharField(
        max_length=4,
        widget=forms.TextInput(attrs={
            'class': 'form-control text-center',
            'placeholder': 'Verification Code',
            'id': 'code',
        })
    )

    def clean(self):
        cleaned_data = super().clean()

        code = cleaned_data.get("code")
        self.user = Code.objects.filter(code=code).first()

        # 2nd .user is to get user 
        if self.user:
            return self.user.user
        else:
            self.add_error(None, "The code is incorrect")


class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()

        password1 = cleaned_data.get("new_password")
        password2 = cleaned_data.get("confirm_password")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data

    def save(self, user, commit=True):
        new_password = self.cleaned_data.get("new_password")
        user.set_password(new_password)

        if commit:
            user.save()
        return user


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email", "phone_number", "profile_photo"]
