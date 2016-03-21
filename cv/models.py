from django.db import models


class Me(models.Model):
    cv_style = models.CharField(max_length=200, blank=False, default="styles.css", choices=[('styles.css', 'Blue'), ('styles-2.css', 'Green-Blue'), ('styles-3.css', 'Green'), ('styles-4.css', 'Purple'), ('styles-5.css', 'Orange'), ('styles-6.css', 'Dark-Blue')])
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    profile_img_url = models.CharField(max_length=200)
    bio = models.TextField(blank=True)

    # cv_language = models.OneToOneField('CvLanguage', unique=True)
    footer = models.CharField(max_length=200)


class ContactRef(models.Model):
    me_ref = models.ForeignKey(Me, related_name="contact_refs")
    ico = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200, blank=True)


class Education(models.Model):
    me_ref = models.ForeignKey(Me, related_name="educations")
    title = models.CharField(max_length=200)
    where = models.CharField(max_length=200, blank=True)
    time_frame = models.CharField(max_length=200, blank=True)
    link = models.CharField(max_length=200, blank=True)


class Language(models.Model):
    me_ref = models.ForeignKey(Me, related_name="languages")
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=200, blank=True, choices=[('', ''), ('Native', 'Native'), ('Fluent', 'Fluent'), ('Intermediate', 'Intermediate'), ('Basic', 'Basic')])


class Interest(models.Model):
    me_ref = models.ForeignKey(Me, related_name="interests")
    name = models.CharField(max_length=200)


class Skills(models.Model):
    me_ref = models.ForeignKey(Me, related_name="skills")
    name = models.CharField(max_length=200)
    value = models.IntegerField()  # 0 and 100


class Experience(models.Model):
    me_ref = models.ForeignKey(Me, related_name="experiences")
    title = models.CharField(max_length=200)
    where = models.CharField(max_length=200, blank=True)
    link = models.CharField(max_length=200, blank=True)
    time_frame = models.CharField(max_length=200, blank=True)
    desc = models.TextField(blank=True)


class ExtraSection(models.Model):
    me_ref = models.ForeignKey(Me, related_name="extra_sections")
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)

    body = models.TextField(blank=True)
