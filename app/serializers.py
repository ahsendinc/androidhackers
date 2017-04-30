from django.contrib.auth.models import User,Group 
from .models import GenericData, Data, BatteryStatus, BatteryHealth, BatteryLevel, BatteryTemperature, CPUTotal, CPUUser, CPUKernel, CPULoad1, CPULoad2, CPULoad3, CPUHog1New, CPUHog2New, CPUHog3New, CPUHog4New, CPUHog5New, MemInfoUsedRam, MemInfoTotalRam, MemInfoFreeRam, TestInfo
from rest_framework import serializers

class TestInfoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = TestInfo
		fields = ('idnum','name','status','message')

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
	def __init__(self, *args, **kwargs):
		many = kwargs.pop('many', True)
		super(BatteryStatusSerializer, self).__init__(many=many, *args, **kwargs)

	class Meta:
		model = BatteryStatus
		fields = ('value','time')

class CPUTotalSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = CPUTotal
		fields = ('time','value')

class CPUUserSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = CPUUser
		fields = ('time','value')

class CPUKernelSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = CPUKernel
		fields = ('time','value')

class CPULoad1Serializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = CPULoad1
		fields = ('time','value')

class CPULoad2Serializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = CPULoad2
		fields = ('time','value')

class CPULoad3Serializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = CPULoad3
		fields = ('time','value')

class CPUHog1Serializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = CPUHog1New
		fields = ('time','value','name')

class CPUHog2Serializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = CPUHog2New
		fields = ('time','value','name')

class CPUHog3Serializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = CPUHog3New
		fields = ('time','value','name')

class CPUHog4Serializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = CPUHog4New
		fields = ('time','value','name')

class CPUHog5Serializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = CPUHog5New
		fields = ('time','value','name')

class MemInfoTotalRamSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = MemInfoTotalRam
		fields = ('time','value')

class MemInfoFreeRamSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = MemInfoFreeRam
		fields = ('time','value')

class MemInfoUsedRamSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = MemInfoUsedRam
		fields = ('time','value')

class MultBatteryStatusSerializer(serializers.Serializer):
    battery_status = BatteryStatusSerializer(many=True)

    def create(self, validated_data):
    	batterystatus_datas = validated_data.pop('battery_status')
    	for batterystatus_data in batterystatus_datas:
		    BatteryStatus.objects.create(**batterystatus_data)


class DataSerializer(serializers.HyperlinkedModelSerializer):
	# battery_status = BatteryStatusSerializer(many=True) 
	# battery_health = BatteryHealthSerializer(many=True)
	# battery_level = BatteryLevelSerializer(many=True)
	# battery_temperature = BatteryTemperatureSerializer(many=True)
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
		fields = ('pubdate',)

	def create(self, validated_data):
		batterystatus_datas = validated_data.pop('batterystatus')
		batteryhealth_datas = validated_data.pop('batteryhealth')
		batterylevel_datas = validated_data.pop('batterylevel')
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