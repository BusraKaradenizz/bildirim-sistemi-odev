classDiagram

&#x20;   class NotificationManager

&#x20;   class EmailNotification

&#x20;   class SMSNotification

&#x20;   class PushNotification

&#x20;   class SMSAdapter



&#x20;   NotificationManager --> EmailNotification

&#x20;   NotificationManager --> SMSNotification

&#x20;   NotificationManager --> PushNotification

&#x20;   NotificationManager --> SMSAdapter



