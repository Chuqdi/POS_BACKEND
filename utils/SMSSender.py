
from django.conf import settings
from twilio.rest import Client


class SMSSender():
    @staticmethod
    def send(text, phone_number):
        
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_ACCOUNT_TOKEN)

        message = client.messages.create(
            to='+2349115494676',
            from_='+12707139596',
            body='test',
        )
        print(message.sid)