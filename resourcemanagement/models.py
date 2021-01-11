from django.db import models
from django.utils.text import slugify
import subprocess
import random
from django.core.mail import send_mail
from django.conf import settings
import os

# Create your models here.


class Application(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, default='')
    email = models.EmailField()
    mobile = models.CharField(max_length=15, default='')
    title = models.CharField(max_length=255)
    application_purpose = models.TextField()
    queries = models.TextField(default='')
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    def generate_password(self):
        t = "abcdefghijkmnopqrstuvwwxyzABCDEFGHIJKLOMNOPQRSTUVWXYZ1234567890"
        return "".join([random.choice(t) for i in range(16)])

    def approve(self, request):
        username = slugify(self.first_name)
        password = self.generate_password()
        subprocess.call(['bash',f'{os.path.join(settings.SCRIPT_DIR, "UserAdd.sh")}', {username}, {password}])
        message = f'Your Application is approved now, user: {username} , password: {password}'
        send_mail(
            from_email='admin@techhimalaya.com', message=message, recipient_list=[self.email, ],
            subject='HPC KU Application Approved'
        )
        self.is_approved = True
