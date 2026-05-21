```mermaid
classDiagram
    class NotificationFactory
    class EmailNotification
    class SMSNotification
    class PushNotification

    NotificationFactory --> EmailNotification
    NotificationFactory --> SMSNotification
    NotificationFactory --> PushNotification
