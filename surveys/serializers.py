from surveys.models import SurveyResponse, Survey
from rest_framework import serializers


class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = ('id', 'name', 'available_places', 'user')


class SurveyResponseSerializer(serializers.ModelSerializer):

    def validate(self, data):
        """
        Check that there are still available places

        """
        try:
            if data['survey'].remaining_places <= 0:
                raise serializers.ValidationError('No survey places remaining, sorry.')
        except AttributeError:
            raise serializers.ValidationError('Incorrect Survey, try again')
        else:
            return data

    class Meta:
        model = SurveyResponse
        fields = ('id', 'survey', 'user', 'created_at')
