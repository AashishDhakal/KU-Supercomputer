from django.db import models

# Create your models here.
class About(models.Model):
    main_headline = models.CharField(max_length=255)
    details = models.TextField()
    where = models.CharField(max_length=100)
    when = models.CharField(max_length=100)
    button_text = models.CharField(max_length=100)
    button_url = models.URLField(max_length=255)
    image = models.ImageField(upload_to='about', help_text="Optimal Resolution: 470 by 629", blank=True, null=True)

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
    facebook_url = models.URLField()
    twitter_url = models.URLField()
    website = models.URLField()

    def __str__(self):
        return self.name


class ContactInquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    inquiry_message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contact Inquiries'