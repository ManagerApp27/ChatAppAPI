import os
import json
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from django.http import HttpResponse
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response

from .models import Message, Contact, Channel
from .serializers import MessageSerializer
from .whatsapp import get_text_user, generate_message
from .openai import get_response_text


class MessageApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['channel', 'contact']
    ordering = ['-timestamp']

    def create(self, request, *args, **kwargs):

        channel_id = request.POST.get("channel")
        contact_id = request.POST.get("contact")
        message = request.POST.get("message")
        message_type = request.POST.get("type")
        origin = request.POST.get("origin")

        contact = Contact.objects.get(id=contact_id)
        id = generate_message(message_type, message, contact.phone)

        query_dict = {
            "id": id,
            "channel": channel_id,
            "contact": contact_id,
            "message": message,
            "type": message_type,
            "origin": origin,
        }

        serializer = self.get_serializer(data=query_dict)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        headers = self.get_success_headers(data)

        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class WhatsAppMessageApiViewSet(APIView):

    def get(self, request):
        verify_token = os.environ.get('WHATSAPP_SECRET_KEY')
        token = request.GET['hub.verify_token']
        challenge = request.GET['hub.challenge']

        try:
            if token != None and challenge != None and token == verify_token:
                return HttpResponse(challenge, status=200)
            else:
                return HttpResponse('error', status=403)

        except:
            return HttpResponse('error', status=403)

    def post(self, request):

        try:
            body = json.loads(request.body)
            entry = (body["entry"])[0]
            changes = (entry["changes"])[0]
            value = changes["value"]
            message = (value["messages"])[0]
            phone_channel = (value["metadata"])["phone_number_id"]
            phone_contact = message["from"]
            type_message = message["type"]
            id = message['id']
            timestamp = int(message['timestamp'])
            timestamp = datetime.fromtimestamp(timestamp)

            try:
                channel = Channel.objects.get(phone=phone_channel)
            except Channel.DoesNotExist:
                return HttpResponse("")

            is_message_exists = Message.objects.filter(id=id).exists()

            if not is_message_exists:

                contact = Contact.objects.get_or_create(
                    user=channel.user,
                    name=phone_contact,
                    phone=phone_contact
                )[0]

                text = get_text_user(message)

                if 'gpt:' in text:
                    response_gpt = get_response_text(text)

                    if response_gpt != "error":
                        generate_message("text", response_gpt, contact.phone)
                        return HttpResponse("EVENT_RECEIVED")
                    else:
                        generate_message("text", "No hubo connexión", contact.phone)
                        return HttpResponse("EVENT_RECEIVED")

                msg = Message(id=id,
                              channel=channel,
                              contact=contact,
                              message=text,
                              timestamp=timestamp,
                              type=type_message,
                              origin="contact",
                              )
                msg.save()

    
                return HttpResponse("EVENT_RECEIVED")
            else:
                return HttpResponse("EVENT_RECEIVED")

        except Exception as e:
            print("Error recivid_message: " + str(e))
            return HttpResponse("EVENT_RECEIVED " + str(e))
