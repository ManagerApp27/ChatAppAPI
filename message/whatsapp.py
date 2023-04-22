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


