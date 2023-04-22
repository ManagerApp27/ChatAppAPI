from django.urls import path
from rest_framework.routers import DefaultRouter
from message.views import MessageApiViewSet, WhatsAppMessageApiViewSet


router_message = DefaultRouter()

router_message.register(prefix='message', basename='message',
                      viewset=MessageApiViewSet)


urlpatterns = [
    path('whatsapp/', WhatsAppMessageApiViewSet.as_view()),
]