from rest_framework.serializers import ModelSerializer
from .models import Message, Chat


class MessageSerializer(ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'


class ChatSerializer(ModelSerializer):

    last_message_data = MessageSerializer(source='last_message', read_only=True)

    class Meta:
        model = Chat
        fields = ['is_group_chat',
                  'channel_id',
                  'contact_id',
                  'last_message',
                  'timestamp',
                  'last_message_data'
                  ]