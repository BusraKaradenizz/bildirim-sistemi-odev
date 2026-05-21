from factory import NotificationFactory

# Bildirimleri factory üzerinden üretelim
bildirim1 = NotificationFactory.create_notification("email")
bildirim1.gonder("Hoş geldiniz!")

bildirim2 = NotificationFactory.create_notification("sms")
bildirim2.gonder("Kodunuz: 1234")

bildirim3 = NotificationFactory.create_notification("push")
bildirim3.gonder("Yeni mesajınız var.")



from notifications.external_sms import ExternalSMSService, SMSAdapter

# Dış servisi kullanmak için adapter
external_service = ExternalSMSService()
sms_adapter = SMSAdapter(external_service)
sms_adapter.gonder("Adapter ile gönderilen SMS!")


from notifications.decorators import LogDecorator, TimestampDecorator
from factory import NotificationFactory

# Normal bildirim
email = NotificationFactory.create_notification("email")

# LogDecorator ile süslenmiş bildirim
loglu_email = LogDecorator(email)
loglu_email.gonder("Decorator ile loglu mesaj!")

# TimestampDecorator ile süslenmiş bildirim
timestamp_email = TimestampDecorator(email)
timestamp_email.gonder("Decorator ile zaman damgalı mesaj!")

# İkisini zincirleme kullanabiliriz
loglu_timestamp_email = LogDecorator(TimestampDecorator(email))
loglu_timestamp_email.gonder("Hem loglu hem zaman damgalı mesaj!")
