from django.contrib import admin
from .models import NiokrCriteria, NiokrProject, NiokrUser, Project, Criteria

admin.site.register(Project)
admin.site.register(Criteria)
admin.site.register(NiokrProject)
admin.site.register(NiokrCriteria)
admin.site.register(NiokrUser)
