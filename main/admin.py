from django.contrib import admin

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


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'email')
    readonly_fields = ('created_date', )


@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', )
    readonly_fields = ('created_date', )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'years', 'created_date')
    readonly_fields = ('created_date', )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'years', 'created_date')
    readonly_fields = ('created_date', )


@admin.register(Award)
class AwdAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'years', 'created_date')
    readonly_fields = ('created_date', )


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date')
    readonly_fields =('created_date', 'modified_date', )


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date')
    readonly_fields = ('created_date', )


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Done)
class DoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'number', 'modified_date')
    readonly_fields = ('modified_date', )


@admin.register(MeContact)
class MeContact(admin.ModelAdmin):
    list_display = ('id', )


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_date')



