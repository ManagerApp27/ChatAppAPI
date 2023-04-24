import os
import json
import requests


def send_message_whatsapp(data):
    try:
        whatsapp_token = os.getenv('WHATSAPP_TOKEN')
        whatsapp_url_version = os.getenv('WHATSAPP_URL_VERSION')
        whatsapp_url_id = os.getenv('WHATSAPP_URL_ID')
        url = f"https://graph.facebook.com/{whatsapp_url_version}/{whatsapp_url_id}/messages"
        headers = {"Content-Type": "application/json",
                   "Authorization": f"Bearer {whatsapp_token}"}

        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()

        result = json.loads(response.text)
        result = (result["messages"])[0]
        return result['id']

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
        return False

    except Exception as e:
        print(f"Error send_message_whatsapp: {e}")
        return False


def get_text_user(message):
    text = ""
    type_message = message["type"]

    if type_message == "text":
        text = (message["text"])["body"]

    elif type_message == "interactive":
        interactive_object = message["interactive"]
        type_interactive = interactive_object["type"]

        if type_interactive == "button_reply":
            text = (interactive_object["button_reply"])["title"]

        elif type_interactive == "list_reply":
            text = (interactive_object["list_reply"])["title"]

        else:
            print("sin mensaje!")

    else:
        print("Sin mensaje!")

    return text


def text_message(text, number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "text",
        "text": {
                "body": text
        }
    }
    return data


def image_message(img, number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "image",
        "image": {
                "link": img
        }
    }

    return data


def audio_message(audio, number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "audio",
        "audio": {
                "link": audio
        }
    }

    return data


def video_message(video, number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "video",
        "video": {
                "link": video
        }
    }

    return data


def document_message(ducument, number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "ducument",
        "ducument": {
                "link": ducument
        }
    }

    return data


def location_message(location, number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "location",
        "location": {
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "name": location["name"],
            "address": location["address"]
        }
    }

    return data


def button_message(button, number):

    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": number,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {
                "text": "Ordenar productos"
            },
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": "001",
                            "title": "Ordenar"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "002",
                            "title": "Cancelar"
                        }
                    }
                ]
            }
        }
    }

    return data


def list_message(list, number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": "✅ I have these options"
            },
            "footer": {
                "text": "Select an option"
            },
            "action": {
                "button": "See options",
                "sections": [
                    {
                        "title": "Buy and sell products",
                        "rows": [
                            {
                                "id": "main-buy",
                                "title": "Buy",
                                "description": "Buy the best product your home"
                            },
                            {
                                "id": "main-sell",
                                "title": "Sell",
                                "description": "Sell your products"
                            }
                        ]
                    },
                    {
                        "title": "📍center of attention",
                        "rows": [
                            {
                                "id": "main-agency",
                                "title": "Agency",
                                "description": "Your can visit our agency"
                            },
                            {
                                "id": "main-contact",
                                "title": "Contact center",
                                "description": "One of our agents will assist you"
                            }
                        ]
                    }
                ]
            }
        }
    }

    return data


def generate_message(type, message, number):
    message_types = {
        "text": text_message,
        "image": image_message,
        "audio": audio_message,
        "video": video_message,
        "document": document_message,
        "location": location_message,
        "button": button_message,
        "list": list_message
    }

    if type in message_types:
        data = message_types[type](message, number)
        id = send_message_whatsapp(data)
        return id
    else:
        pass
