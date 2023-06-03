from rest_framework.routers import DefaultRouter
from .views import ChannelApiViewSet, WhatsAppTokensApiViewSet


router_channel = DefaultRouter()

router_channel.register(prefix='channel', 
                        basename='channel', 
                        viewset=ChannelApiViewSet)

router_channel.register(prefix='wat', 
                        basename='wat', 
                        viewset=WhatsAppTokensApiViewSet)