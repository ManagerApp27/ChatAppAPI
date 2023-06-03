from rest_framework.serializers import ModelSerializer
from .models import Channel, WhatsAppTokens


class ChannelSerializer(ModelSerializer):

    class Meta:
        model = Channel
        fields = '__all__'


class WhatsAppTokensSerializer(ModelSerializer):

    class Meta:
        model = WhatsAppTokens
        fields = '__all__'