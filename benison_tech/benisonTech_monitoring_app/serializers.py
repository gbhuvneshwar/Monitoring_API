from rest_framework import serializers

from benisonTech_monitoring_app.models import Devices, UserProfile


class DevicesSerializer(serializers.ModelSerializer):
    device_name = serializers.CharField(max_length=100)
    device_status = serializers.BooleanField(default=False)
    cpu_utilization = serializers.CharField(max_length=100)
    memory_utilization =  serializers.CharField(max_length=1000)

    class Meta:
        model = Devices
        fields = ('device_name', 'device_status', 'cpu_utilization', 'memory_utilization')



class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = UserProfile
        fields = ('email',)


