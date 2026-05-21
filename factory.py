from notifications.email import EmailNotification
from notifications.sms import SMSNotification
from notifications.push import PushNotification

class NotificationFactory:
    @staticmethod
    def create_notification(tip):
        if tip == "email":
            return EmailNotification()
        elif tip == "sms":
            return SMSNotification()
        elif tip == "push":
            return PushNotification()
        else:
            raise ValueError("Bilinmeyen bildirim tipi!")
