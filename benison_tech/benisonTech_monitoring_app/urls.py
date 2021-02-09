from django.contrib import admin


from django.urls import path
from django.conf.urls import url

from benisonTech_monitoring_app import views 

urlpatterns = [
			   path("monitoring-devices/", views.MonitoringApiView.as_view()),
			   ]