# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from surveys.models import Survey, SurveyResponse


class SurveyAdmin(admin.ModelAdmin):
    list_display = ['name', 'available_places', 'user',]

    search_fields = ['name', 'user__email',]


class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = ['survey', 'user',]


admin.site.register(Survey, SurveyAdmin)
admin.site.register(SurveyResponse, SurveyResponseAdmin)