\# A – Bildirim Sistemi



\## 🎯 Gerekçe

Başlangıçta tüm bildirim tipleri (e‑posta, SMS, push) tek bir sınıfta if‑else zincirleriyle kontrol ediliyordu. Bu yapı esnek değildi ve yeni bildirim tipleri eklemek mevcut kodu kırıyordu. Bu nedenle \*\*Bildirim Sistemi\*\* konusunu seçtim.



\---



\## 📌 Proje Tanımı

Bu proje, farklı kanallardan (Email, SMS, Push, External SMS) bildirim göndermeyi sağlayan bir sistemdir. Tasarım örüntüleri kullanılarak sistem esnek, genişletilebilir ve bakımı kolay hale getirilmiştir.



\---



\## 🛠 Kullanılan Tasarım Örüntüleri

\- \*\*Factory Pattern (Faz 1)\*\* → Bildirim nesnelerinin oluşturulmasını merkezi bir yapıya taşıdı.  

\- \*\*Adapter Pattern (Faz 2)\*\* → Harici SMS servislerini sisteme entegre etti.  

\- \*\*Decorator Pattern (Faz 2)\*\* → Bildirimlere ek özellikler (loglama, zaman damgası) kazandırdı.  

\- \*\*Observer Pattern (Faz 3)\*\* → Tek bir olayla birden fazla bildirim kanalını tetikledi.  



\---



\## 🖼 Mimari Diyagram

(Diagramı draw.io veya mermaid ile çizebilirsin. Örnek mermaid kodu:)



```mermaid

classDiagram

&#x20;   class NotificationFactory

&#x20;   class EmailNotification

&#x20;   class SMSNotification

&#x20;   class PushNotification

&#x20;   class SMSAdapter

&#x20;   class LogDecorator

&#x20;   class TimestampDecorator

&#x20;   class NotificationManager



&#x20;   NotificationFactory --> EmailNotification

&#x20;   NotificationFactory --> SMSNotification

&#x20;   NotificationFactory --> PushNotification

&#x20;   SMSAdapter --> ExternalSMSService

&#x20;   LogDecorator --> EmailNotification

&#x20;   TimestampDecorator --> EmailNotification

&#x20;   NotificationManager --> EmailNotification

&#x20;   NotificationManager --> SMSNotification

&#x20;   NotificationManager --> PushNotification

&#x20;   NotificationManager --> SMSAdapter



