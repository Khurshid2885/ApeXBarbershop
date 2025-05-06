from django import forms
from django.contrib.auth.models import Group

from services.models import Service, Appointment
from accounts.models import CustomUser, BarberProfile
from services.models.service import ServiceCategory


# It is for Admins-Only

class BarberCreateForm(forms.ModelForm):
    username = forms.CharField(max_length=10, required=True)
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(widget=forms.EmailInput(), required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    img_file = forms.FileField(required=False)

    class Meta:
        model = BarberProfile
        fields = ['bio', 'experience_years', 'rating']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        rating = cleaned_data.get("rating")

        # User already exists
        if username and CustomUser.objects.filter(username=username).exists():
            self.add_error(None, "This user already exists.")

        # Validate rating (must be between 1 and 5)
        if not rating or (rating < 0 or rating > 5):
            self.add_error(None, "Rating MUST be in range (1, 5).")

        # # No File Upload
        # if not cleaned_data.get("img_file"):
        #     self.add_error(None, "You have to upload a barber image.")

        return cleaned_data

    def save(self, commit=True):
        cleaned_data = self.cleaned_data

        user = CustomUser.objects.create_user(
            username=cleaned_data.get("username"),
            first_name=cleaned_data.get("first_name"),
            last_name=cleaned_data.get("last_name"),
            email=cleaned_data.get("email"),
            phone_number=cleaned_data.get("phone_number"),
            password=cleaned_data.get("password")
        )

        user.set_password(cleaned_data.get("password"))
        user.save()

        barber = BarberProfile.objects.create(
            bio=cleaned_data.get("bio"),
            experience_years=cleaned_data.get("experience_years"),
            rating=cleaned_data.get("rating"),
            user=user,
        )

        if cleaned_data.get("img_file"):
            barber.image = cleaned_data.get("img_file")

        if commit:
            barber.save()
        return user  # If I return barber, BarberProfile is not linked to Group Model.
        # I can't assign barber to barber group.


class BarberEditForm(forms.ModelForm):
    username = forms.CharField(max_length=10, required=True)
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(widget=forms.EmailInput(), required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    img_file = forms.FileField(required=False)

    # Select services
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control', 'size': '5'}),
        required=False
    )

    class Meta:
        model = BarberProfile
        fields = ['bio', 'experience_years', 'image', 'rating', "services"]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.user_instance = kwargs.pop("user_instance", None)
        super().__init__(*args, **kwargs)

        # Prefill fields from User model
        if self.user_instance:
            self.fields["username"].initial = self.user_instance.username
            self.fields["first_name"].initial = self.user_instance.first_name
            self.fields["last_name"].initial = self.user_instance.last_name
            self.fields["email"].initial = self.user_instance.email
            self.fields["phone_number"].initial = self.user_instance.phone_number

    def save(self, commit=True):
        barber = super().save(commit=False)
        cleaned_data = self.cleaned_data

        if self.user_instance:
            self.user_instance.username = cleaned_data.get("username")
            self.user_instance.first_name = cleaned_data.get("first_name")
            self.user_instance.last_name = cleaned_data.get("last_name")
            self.user_instance.email = cleaned_data.get("email")
            self.user_instance.phone_number = cleaned_data.get("phone_number")
            self.user_instance.save()

        if self.cleaned_data.get("img_file"):
            barber.image = self.cleaned_data.get("img_file")

        services = self.cleaned_data.get("services")
        if services:
            barber.services.set(services)

        if commit:
            barber.save()

        return barber


class HaircutCreateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["name", "description", "price", "duration", "barber", "img_file"]


class HaircutEditForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["name", "description", "price", "duration", "barber", "img_file"]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class UserEditForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),  # Get all groups
        widget=forms.SelectMultiple(attrs={'class': 'form-select'}),  # Multi-select
        required=False
    )

    class Meta:
        model = CustomUser
        fields = ["username", "email", "phone_number", "is_active", "groups"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = ServiceCategory
        fields = ["name", "main_image"]


class CategoryEditForm(forms.ModelForm):
    class Meta:
        model = ServiceCategory
        fields = ["name", "main_image"]


class ServiceCreateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["img_file", "name", "description", "price", "duration"]


class ServiceEditForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["img_file", "name", "description", "price", "duration"]


# It is for Barbers-Only
class BarberAppointmentEditForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['status']
