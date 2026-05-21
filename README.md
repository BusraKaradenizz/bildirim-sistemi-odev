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






