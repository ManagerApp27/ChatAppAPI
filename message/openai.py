import openai
import os


def get_response_text(prompt):
    try:
        openai.api_key = os.getenv('OPENAI_API_KEY')
        result = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0,
            n=1,
            stop=None,
            max_tokens=1000
        )

        response = result.choices[0].text

        return response

    except Exception as e:
        print(e)

        return "error"


def get_response_image(prompt, n):

    try:
        openai.api_key = os.getenv('OPENAI_API_KEY')
        response = openai.Image.create(
            prompt=prompt,
            n=2,
            size="1024x1024"
        )
        image_url = response['data']

        return image_url

    except Exception as e:
        print(e)

        return "error"