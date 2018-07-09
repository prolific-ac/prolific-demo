from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from surveys import views as survey_views
from profiles import views as profile_views

router = routers.DefaultRouter()

router.register(r'surveys', survey_views.SurveyViewSet)
router.register(r'survey-responses', survey_views.SurveyResponseViewSet)
router.register(r'profiles', profile_views.MemberViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls))
]
