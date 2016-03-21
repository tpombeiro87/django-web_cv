from django.shortcuts import render

from cv.models import *


def index(request):
    user = Me.objects.get(id=1)
    template_data = {
        'user': user,
        'contact_refs': user.contact_refs.all(),
        'educations': user.educations.all(),
        'languages': user.languages.all(),
        'interests': user.interests.all(),
        'skills': user.skills.all(),
        'experiences': user.experiences.all(),
        'extra_sections': user.extra_sections.all()
    }
    return render(request, 'index.html', template_data)
