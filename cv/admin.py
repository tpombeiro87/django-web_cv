from django.contrib.auth.models import Group
from django.contrib import admin

from models import *


admin.site.unregister(Group)


class ContactRefInline(admin.TabularInline):
    model = ContactRef
    extra = 0


class EducationInline(admin.TabularInline):
    model = Education
    extra = 0


class LanguageInline(admin.TabularInline):
    model = Language
    extra = 0


class InterestInline(admin.TabularInline):
    model = Interest
    extra = 0


class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 0


class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 0


class ExtraSectionInline(admin.StackedInline):
    model = ExtraSection
    extra = 0


class MeAdmin(admin.ModelAdmin):
    model = Me

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    '''def has_delete_permission(request, obj=None):
        return False
    '''
    fieldsets = (
        ('Right Side Top', {
            'fields': ('cv_style', 'name', 'title', 'profile_img_url', 'bio', 'footer')
        }),
        # ('Right Side Below', {
        #    'fields': ('contact_refs', 'educations', 'languages')
        # }),
        # ('Main', {
        #    'fields': ('bio', 'experiences', 'extra_sections', 'footer')
        # }),
    )
    inlines = [
        ContactRefInline,
        EducationInline,
        LanguageInline,
        InterestInline,
        SkillsInline,
        ExperienceInline,
        ExtraSectionInline,
    ]

    class Media:
        js = ('3rdparty/tinymce/tinymce.min.js', 'custom.js')
        css = {
             'all': ('custom.css',)
        }


admin.site.register(Me, MeAdmin)
