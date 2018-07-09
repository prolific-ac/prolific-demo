# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets

from surveys.models import SurveyResponse, Survey

from surveys.serializers import SurveySerializer, SurveyResponseSerializer


class SurveyViewSet(viewsets.ModelViewSet):
    """
    API Endpoint to allow survey viewing or editing
    """
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user',)


class SurveyResponseViewSet(viewsets.ModelViewSet):
    """
    API Endpoint to allow survey viewing or editing
    """
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('survey', 'user',)