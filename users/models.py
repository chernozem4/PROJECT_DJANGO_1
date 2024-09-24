from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(User):
    DEVELOPER_LEVELS = (
        ('junior', 'Junior Developer'),
        ('middle', 'Middle Developer'),
        ('senior', 'Senior Developer'),
    )

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    phone_number = models.CharField(max_length=14, default='+996')
    age = models.PositiveIntegerField(
        default=10,
        validators=[
            MaxValueValidator(99),
            MinValueValidator(5),
        ]
    )
    gender = models.CharField(max_length=10, choices=GENDER)

    # Developer level and salary fields
    level = models.CharField(max_length=10, choices=DEVELOPER_LEVELS, default='junior')
    salary = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.username


# Signal to set the salary based on the developer level after the user is created
@receiver(post_save, sender=CustomUser)
def set_salary(sender, instance, created, **kwargs):
    if created:
        print("Signal processed: user created")
        level = instance.level
        if level == 'junior':
            instance.salary = 500
        elif level == 'middle':
            instance.salary = 1000
        elif level == 'senior':
            instance.salary = 3000
        else:
            instance.salary = 0  # Default value if the level is undefined
        instance.save()


