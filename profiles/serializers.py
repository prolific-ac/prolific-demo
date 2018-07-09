from profiles.models import Member
from rest_framework import serializers


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = ('id', 'username', 'email', 'first_name', 'last_name')