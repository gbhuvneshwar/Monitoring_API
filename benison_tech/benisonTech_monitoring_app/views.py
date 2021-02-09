from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.serializers import serialize
from django.core.mail import EmailMessage
from django.conf import settings

from benisonTech_monitoring_app.models import Devices, UserProfile
from benisonTech_monitoring_app import serializers


import distro
import psutil
import time

class MonitoringApiView(APIView):

    def send_email(self, mail_subject=None, mail_content=None):
        
        to_mail = ["b.chouksey27@protonmail.com"]    
        all_users = UserProfile.objects.all()   

        for i in all_users:
            to_mail.append(i.email)

        from_mail = settings.EMAIL_HOST_USER
        
        email = EmailMessage(mail_subject, mail_content, from_mail, to_mail)
        email.send()            

    
    def get(self, request, pk=None):

        deviceslist_serializer = serializers.DevicesSerializer

        all_entries = Devices.objects.all()

        CPU_UTILIZATION_THRESHOLD = 90.0 # In percentage 90%
        PHYSICAL_MEMORY_THRESHOLD = 10 * 1024 * 1024 * 1024 # 10 GB
        RAM_THRESHOLD = 3*1024 * 1024 * 1024 # 3GB
        

        for i in all_entries:

            i.device_status = True     
            cpu_utliz = psutil.cpu_percent()

            if cpu_utliz >= CPU_UTILIZATION_THRESHOLD:
                mail_subject = "CPU_UTILIZATION_THRESHOLD_REACHED"
                mail_content = "CPU utilization reached threshold Please take urgent action"                
                self.send_email(mail_subject, mail_content)

            mem = psutil.virtual_memory()
            physical_memory = mem.available

            if physical_memory >= PHYSICAL_MEMORY_THRESHOLD:
                mail_subject = "Memory_UTILIZATION_THRESHOLD_REACHED"
                mail_content = "Memory utilization reached threshold Please take urgent action"
                self.send_email(mail_subject, mail_content)
    

            i.cpu_utilization = str(cpu_utliz) + "%"
            i.memory_utilization = mem
            i.save()
            time.sleep(2)

        serializer = deviceslist_serializer(all_entries, many=True)

        #email = EmailMessage(mail_subject,mail_content,from_mail,to_mail)
        #email.send()

        data = serializer.data
        return Response(serializer.data)

        