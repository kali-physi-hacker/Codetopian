from django.db import models


STACK_CHOICES = (
    ("Python", "python"),
    ("Java", "java"),
    ("C/C++", "c/c++"),
    ("Android Application Development", "android_app_dev"),
    ("Django", "django"),
    ("Ruby On Rails", "ruby_on_rails"),
    ("Flask", "flask"),
    ("Nodejs", "nodejs"),
    ("ExpressJS", "express"),
    ("ReactJS", "react"),
    ("AngularJS", "angular"),
    ("VueJS", "vue"),
    ("Flask", "flask"),
)

class Developer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.PositiveIntegerField(null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    stack = models.CharField(max_length=500, null=True, blank=True)
    organisation = models.CharField(max_length=200, blank=True, null=True)
    years_of_experience = models.PositiveIntegerField(null=True, blank=True)


    def __str__(self):
        return "{} {} - <{}>".format(
            self.first_name, self.last_name, self.email_address
        )

    def all_stacks(self):
        return STACK_CHOICES