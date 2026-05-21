# Kullanılan Tasarım Örüntüleri

## Faz 1 – Creational
### Factory Pattern
- **Nerede kullandım?** Bildirim nesnelerinin (Email, SMS, Push) oluşturulmasında.  
- **Neden seçtim?** Nesne yaratma sorumluluğunu merkezi bir yapıya taşımak için.  
- **Ne kazandırdı?** Kod tekrarını azalttı, yeni bildirim tipleri eklemeyi kolaylaştırdı.

---

## Faz 2 – Structural
### Adapter Pattern
- **Nerede kullandım?** Harici SMS servislerini sisteme entegre etmek için.  
- **Neden seçtim?** Mevcut kodu değiştirmeden yeni servis ekleyebilmek için.  
- **Ne kazandırdı?** Esneklik ve genişletilebilirlik sağladı.

### Decorator Pattern
- **Nerede kullandım?** Bildirimlere loglama ve zaman damgası eklemek için.  
- **Neden seçtim?** Bildirimlere ek özellikler kazandırmak için mevcut sınıfları değiştirmek istemedim.  
- **Ne kazandırdı?** Modülerlik ve Açık/Kapalı prensibine uygunluk sağladı.

---

## Faz 3 – Behavioral
### Observer Pattern
- **Nerede kullandım?** Tek bir olayla birden fazla bildirim kanalını tetiklemek için.  
- **Neden seçtim?** Yeni bildirim kanalları eklenirken mevcut kodu değiştirmemek için.  
- **Ne kazandırdı?** Açık/Kapalı prensibine uygunluk, çoklu kanal desteği.
