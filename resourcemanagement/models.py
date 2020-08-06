from django.db import models
from django.utils.text import slugify
import subprocess
import random
from django.core.mail import send_mail
from django.conf import settings
import os

# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    institution = models.CharField(max_length=255)
    employment_type = models.CharField(choices=(
        ('Faculty', 'Faculty'),
        ('Researcher', 'Researcher'),
        ('Student', 'Student'),
    ), max_length=20)
    application_purpose = models.TextField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}, {self.employment_type} at {self.institution}'

    def generate_password(self):
        t = "abcdefghijkmnopqrstuvwwxyzABCDEFGHIJKLOMNOPQRSTUVWXYZ1234567890"
        return "".join([random.choice(t) for i in range(16)])

    def approve(self, request):
        username = slugify(self.name)
        password = self.generate_password()
        subprocess.call(['bash',f'{os.path.join(settings.SCRIPT_DIR, "UserAdd.sh")}', {username}, {password}])
        message = f'Your Application is approved now, user: {username} , password: {password}'
        send_mail(
            from_email='admin@techhimalaya.com', message=message, recipient_list=[self.email, ],
            subject='HPC KU Application Approved'
        )
        self.is_approved = True
