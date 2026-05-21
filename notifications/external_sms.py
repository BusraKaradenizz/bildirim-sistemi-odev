class ExternalSMSService:
    def send_message(self, text):
        print(f"[EXTERNAL SMS] {text}")


class SMSAdapter:
    def __init__(self, external_service):
        self.external_service = external_service

    def gonder(self, mesaj):
        # Sistemde kullanılan arayüzü dış servise uyarlıyoruz
        self.external_service.send_message(mesaj)
