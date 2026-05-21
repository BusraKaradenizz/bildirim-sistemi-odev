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
