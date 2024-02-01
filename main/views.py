from django.shortcuts import render

from .models import (AboutMe,
                     Occupation,
                     Partner,
                     Education,
                     Experience,
                     Award,
                     Skills,
                     Services,
                     Projects,
                     Done,
                     MeContact,
                     Contacts
                     )


def home_view(request):
    about = AboutMe.objects.get()
    partner = Partner.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    skills_top = Skills.objects.all()[:3]
    skills = Skills.objects.all()[3:]
    awards = Award.objects.all()
    services = Services.objects.all()
    projects = Projects.objects.all()
    done = Done.objects.all()
    mecontact = MeContact.objects.get()
    print(mecontact.address)

    context = {
        'about': about,
        'partner': partner,
        'education': education,
        'experience': experience,
        'skills': skills,
        'skills_top': skills_top,
        'awards': awards,
        'services': services,
        'projects': projects,
        'done': done,
        'mecontact': mecontact,

    }
    return render(request, 'main/index.html', context)


