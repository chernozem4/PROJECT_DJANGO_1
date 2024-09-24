from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Developer levels and genders
DEVELOPER_LEVELS = (
    ('junior', 'Junior Developer'),
    ('middle', 'Middle Developer'),
    ('senior', 'Senior Developer'),
)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

# Custom registration form with developer level
class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    level = forms.ChoiceField(choices=DEVELOPER_LEVELS, required=True)  # New field for developer level

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'gender',
            'phone_number',
            'level'  # Add level to form fields
        )

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# Signal to set the salary based on developer level
@receiver(post_save, sender=models.CustomUser)
def set_salary(sender, instance, created, **kwargs):
    if created:
        level = instance.level
        # Assign salary based on the developer's level
        if level == 'junior':
            instance.salary = 500
        elif level == 'middle':
            instance.salary = 1000
        elif level == 'senior':
            instance.salary = 3000
        else:
            instance.salary = 0  # Default if level is undefined
        instance.save()
