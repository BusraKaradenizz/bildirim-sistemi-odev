\# A – Bildirim Sistemi



\## Gerekçe

Başlangıçta tüm bildirim tipleri (e‑posta, SMS, push) tek bir sınıfta if‑else zincirleriyle kontrol ediliyordu. Bu yapı esnek değildi ve yeni bildirim tipleri eklemek mevcut kodu kırıyordu. Bu nedenle \*\*Bildirim Sistemi\*\* konusunu seçtim.



\---



\## Proje Tanımı

Bu proje, farklı kanallardan (Email, SMS, Push, External SMS) bildirim göndermeyi sağlayan bir sistemdir. Tasarım örüntüleri kullanılarak sistem esnek, genişletilebilir ve bakımı kolay hale getirilmiştir.



\---



\## Kullanılan Tasarım Örüntüleri

\- \*\*Factory Pattern (Faz 1)\*\* → Bildirim nesnelerinin oluşturulmasını merkezi bir yapıya taşıdı.

\- \*\*Adapter Pattern (Faz 2)\*\* → Harici SMS servislerini sisteme entegre etti.

\- \*\*Decorator Pattern (Faz 3)\*\* → Bildirimlere ek özellikler (loglama, zaman damgası) kazandırdı.

\- \*\*Observer Pattern (Faz 4)\*\* → Tek bir olayla birden fazla bildirim kanalını tetikledi.



\---


Bildirim sistemi ödevi kapsamında aşağıdaki dosyalar ve klasörler hazırlanmıştır:  



\- \*\*Ana klasör\*\*  

&#x20; - `main.py`, `factory.py`, `notifications/` → Bildirim sistemi kodları  

&#x20; - `README.md` → Proje tanımı, çalışma talimatları  

&#x20; - `PATTERNS.md` → Kullanılan tasarım örüntülerinin açıklamaları  

&#x20; - `PROBLEMS.md` → Karşılaşılan sorunlar ve çözümler  



\- \*\*docs/\*\*  

&#x20; - `ai-log/phase1.md`, `phase2.md`, `phase3.md` → AI log dosyaları  

&#x20; - `diagrams/faz1.md`, `faz2.md`, `faz3.md` → UML diyagramları (Mermaid ile hazırlanmış)  



\- \*\*.github/workflows/\*\*  

&#x20; - `ci.yml` → CI pipeline dosyası (her push sonrası otomatik test çalıştırır)  



Saygılarımla,  

\*\*Büşra Karadeniz\*\*

