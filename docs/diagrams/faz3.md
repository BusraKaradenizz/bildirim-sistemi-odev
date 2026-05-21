```mermaid
classDiagram
    class NotificationManager
    class EmailNotification
    class SMSNotification
    class PushNotification
    class SMSAdapter

    NotificationManager --> EmailNotification
    NotificationManager --> SMSNotification
    NotificationManager --> PushNotification
    NotificationManager --> SMSAdapter
