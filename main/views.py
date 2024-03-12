from django.shortcuts import render, redirect
from django.contrib import messages


from article.models import Article
from .forms import ContactsForm
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
                     )


def home_view(request):
    occupations = Occupation.objects.all()
    about = AboutMe.objects.get()
    partner = Partner.objects.all()
    awards = Award.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    skills_top = Skills.objects.all()[:3]
    skills = Skills.objects.all()[3:]
    services = Services.objects.all()
    projects = Projects.objects.all()
    done = Done.objects.all()
    articles = Article.objects.order_by('id')[:3]
    mecontact = MeContact.objects.get()
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact successfully add')
            return redirect('.#contact-formm')
    form = ContactsForm()
    context = {
        'occupations': occupations,
        'about': about,
        'partner': partner,
        'awards': awards,
        'education': education,
        'experience': experience,
        'skills': skills,
        'skills_top': skills_top,
        'services': services,
        'projects': projects,
        'done': done,
        'articles': articles,
        'mecontact': mecontact,
        'form': form,
    }
    return render(request, 'main/index.html', context)


