from rest_framework import serializers
from InfoData.models import InfoModal

class InfoModalSerializer(serializers.ModelSerializer):

    class Meta:
        model = InfoModal
        fields = '__all__'