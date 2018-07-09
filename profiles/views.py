# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets

from profiles.models import Member
from profiles.serializers import MemberSerializer


class MemberViewSet(viewsets.ModelViewSet):
    """
    API Endpoint to allow survey viewing or editing
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer