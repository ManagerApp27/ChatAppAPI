from rest_framework.routers import DefaultRouter
from contact.views import ContactApiViewSet


router_contact = DefaultRouter()

router_contact.register(prefix='contact', basename='contact',
                      viewset=ContactApiViewSet)