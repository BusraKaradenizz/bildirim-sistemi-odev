class BildirimSistemi:
    def __init__(self, tip):
        self.tip = tip

    def gonder(self, mesaj):
        if self.tip == "email":
            print(f"[EMAIL] {mesaj}")
        elif self.tip == "sms":
            print(f"[SMS] {mesaj}")
        elif self.tip == "push":
            print(f"[PUSH] {mesaj}")
        else:
            print("Bilinmeyen bildirim tipi!")

# Kullanım örnekleri
bildirim1 = BildirimSistemi("email")
bildirim1.gonder("Hoş geldiniz!")

bildirim2 = BildirimSistemi("sms")
bildirim2.gonder("Kodunuz: 1234")

bildirim3 = BildirimSistemi("push")
bildirim3.gonder("Yeni mesajınız var.")
