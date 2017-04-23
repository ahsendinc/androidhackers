from django.contrib.auth.models import User,Group 
from .models import GenericData, Data, BatteryStatus, BatteryHealth, BatteryLevel, BatteryTemperature
from rest_framework import serializers

class BatteryLevelSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = BatteryLevel
		fields = ('time','value')

class BatteryTemperatureSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = BatteryTemperature
		fields = ('time','value')

class BatteryHealthSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = BatteryHealth
		fields = ('time','value')

class BatteryStatusSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = BatteryStatus
		fields = ('time','value')

class DataSerializer(serializers.HyperlinkedModelSerializer):
	battery_status = BatteryStatusSerializer(many=True) 
	battery_health = BatteryHealthSerializer(many=True)
	battery_level = BatteryLevelSerializer(many=True)
	battery_temperature = BatteryTemperatureSerializer(many=True)
	# cpu_total =  
	# cpu_load1
	# cpu_load2
	# cpu_load3
	# cpu_app1
	# cpu_app2
	# cpu_app3
	# meminfo_totalRAM
	# meminfo_total_freeRAM
	# meminfo_total_usedRAM

	class Meta:
		model = Data
		fields = ('pubdate', 'battery_status', 'battery_health', 'battery_level', 'battery_temperature')

	def create(self, validated_data):
		batterystatus_datas = validated_data.pop('battery_status')
		batteryhealth_datas = validated_data.pop('battery_health')
		batterylevel_datas = validated_data.pop('battery_level')
		batterytemperature_datas = validated_data.pop('battery_temperature')
		data = Data.objects.create(**validated_data)
		for batterystatus_data in batterystatus_datas:
		    BatteryStatus.objects.create(data=data, **batterystatus_data)

		for batteryhealth_data in batteryhealth_datas:
		    BatteryHealth.objects.create(data=data, **batteryhealth_data)

		for batterylevel_data in batterylevel_datas:
		    BatteryLevel.objects.create(data=data, **batterylevel_data)

		for batterytemperature_data in batterytemperature_datas:
		    BatteryTemperature.objects.create(data=data, **batterytemperature_data)

		return data

class GenericDataSerializer(serializers.HyperlinkedModelSerializer):
	#batterystatus = BatteryStatusSerializer(many = True)
	#multipledata = serializers.HyperlinkedRelatedField(many = True)
	class Meta:
		model = GenericData
		fields=('pubdate','jsondata')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')