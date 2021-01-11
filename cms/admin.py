from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ['details', ]
    list_display = ['main_headline', 'image']


class EventAdmin(SummernoteModelAdmin):
    summernote_fields = ['about', ]
    prepopulated_fields = {'slug': ('title',)}


class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ['detail', ]
    list_display = ['title', 'published_date', 'category']
    search_fields = ['title', ]
    filter_fields = ['category', 'published_date']
    prepopulated_fields = {'slug': ('title',)}


class SponsorAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo', 'partner_type', 'website']


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['image_title', 'image']


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['photo', 'name' , 'designation']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['subject', 'email']


admin.site.register(About, AboutAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(ContactInquiry, ContactAdmin)
admin.site.register(FAQ)
admin.site.register(Event, EventAdmin)