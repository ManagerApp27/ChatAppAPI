from rest_framework.viewsets import ModelViewSet
from rest_framework import status
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
        tokens_queryset = WhatsAppTokens.objects.filter(channel_id=channel)
        tokens_serializer = WhatsAppTokensSerializer(tokens_queryset, many=True)
        return tokens_serializer.data

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        for index, instance in enumerate(queryset):
            tokens = self.get_tokens(instance)
            data[index]['tokens'] = tokens
        return Response(data, status=status.HTTP_200_OK)


class WhatsAppTokensApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WhatsAppTokensSerializer
    queryset = WhatsAppTokens.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['channel_id']
    ordering = ['-created']