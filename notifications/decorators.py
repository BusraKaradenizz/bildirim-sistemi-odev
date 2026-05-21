class LogDecorator:
    def __init__(self, notification):
        self.notification = notification

    def gonder(self, mesaj):
        print(f"[LOG] Mesaj gönderiliyor: {mesaj}")
        self.notification.gonder(mesaj)


import datetime

class TimestampDecorator:
    def __init__(self, notification):
        self.notification = notification

    def gonder(self, mesaj):
        zaman = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        yeni_mesaj = f"{zaman} - {mesaj}"
        self.notification.gonder(yeni_mesaj)
