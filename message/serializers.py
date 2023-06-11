from rest_framework.serializers import ModelSerializer
from .models import Message, Chat
from contact.serializers import ContactSerializer

class MessageSerializer(ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'


class ChatSerializer(ModelSerializer):

    last_message_data = MessageSerializer(source='last_message', read_only=True)
    contact_data = ContactSerializer(source='contact_id', read_only=True)

    class Meta:
        model = Chat
        fields = ['id',
                  'is_group_chat',
                  'channel_id',
                  'contact_id',
                  'last_message',
                  'timestamp',
                  'last_message_data',
                  'contact_data'
                  ]