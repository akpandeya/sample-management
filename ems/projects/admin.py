from django.contrib import admin
from .models import Project, Sample, Experiment, Measurement, Machine

admin.site.register(Project)
admin.site.register(Measurement)
admin.site.register(Machine)
admin.site.register(Sample)
admin.site.register(Experiment)

admin.site.site_header = "Avanindra's Experiment Management System"