from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Channel, WhatsAppTokens
from .serializers import ChannelSerializer, WhatsAppTokensSerializer


class ChannelApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ChannelSerializer
    queryset = Channel.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['user_id']
    ordering = ['-created']

    def get_tokens(self, channel):
        tokens_queryset = WhatsAppTokens.objects.filter(channel_id=channel.id)
        tokens_serializer = WhatsAppTokensSerializer(tokens_queryset, many=True)
        return tokens_serializer.data

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        tokens = self.get_tokens(instance)
        data = serializer.data
        data['tokens'] = tokens
        return Response(data)


class WhatsAppTokensApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WhatsAppTokensSerializer
    queryset = WhatsAppTokens.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['channel_id']
    ordering = ['-created']