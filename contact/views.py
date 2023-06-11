from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from contact.models import Contact
from contact.serializers import ContactSerializer


class ContactApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['user_id', 'channel_id', 'phone']
    ordering = ['-created']