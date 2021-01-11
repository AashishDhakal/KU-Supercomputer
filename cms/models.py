from django.db import models

# Create your models here.


class About(models.Model):
    main_headline = models.CharField(max_length=255)
    details = models.TextField()
    button_text = models.CharField(max_length=100)
    button_url = models.URLField(max_length=255)
    image = models.ImageField(upload_to='about', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    video_title = models.CharField(max_length=50, default='')
    video_description = models.TextField(default='')
    video_button_text = models.CharField(max_length=30, default='')
    video_button_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.main_headline

    class Meta:
        verbose_name_plural = 'About'


class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='news')
    detail = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'News'


class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='sponsor')
    partner_type = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    image_title = models.CharField(max_length=255)

    def __str__(self):
        return self.image_title

    class Meta:
        verbose_name_plural = 'Galleries'


class TeamMember(models.Model):
    photo = models.ImageField(upload_to='teams')
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name


class ContactInquiry(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, default='')
    mobile = models.CharField(max_length=15, default='')
    email = models.EmailField()
    subject = models.CharField(max_length=255, default='')
    inquiry_message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contact Inquiries'


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Event(models.Model):
    thumbnail = models.ImageField(upload_to='events')
    title = models.CharField(max_length=255)
    slug = models.SlugField(default='')
    speaker = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    about = models.TextField()
    event_date = models.DateTimeField()
    price = models.CharField(max_length=100)
    registration_link = models.URLField()
    venue = models.TextField()

    def __str__(self):
        return self.title
