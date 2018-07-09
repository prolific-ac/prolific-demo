# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError

from django.db import models
from django.conf import settings



class Survey(models.Model):
    name = models.CharField(max_length=128, help_text='Name of the survey as you want it to appear on the site')
    available_places = models.PositiveIntegerField(null=False, blank=False, help_text='Limit of entries submitted')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    @property
    def remaining_places(self):
        return self.available_places - SurveyResponse.objects.filter(survey_id=self.pk).count()

    def __unicode__(self):
        return u'{0}'.format(self.name)


class SurveyResponse(models.Model):

    survey = models.ForeignKey(Survey)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.pk:
            # creating a new response
            if self.survey.remaining_places <= 0:
                raise ValidationError('There are no remaining survey places left.')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.pk:
            # creating a new response
            if self.survey.remaining_places > 0:
                super(SurveyResponse, self).save(force_insert=False, force_update=False, using=None,
             update_fields=None)
            else:
                raise ValidationError('There are no remaining survey places left.')
