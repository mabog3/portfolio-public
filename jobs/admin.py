from django.contrib import admin
from .models import Job, Skill, Project, Host, Club

# Register your models here.

admin.site.register(Job)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Host)
admin.site.register(Club)