```mermaid
classDiagram
    class NotificationFactory
    class EmailNotification
    class SMSNotification
    class PushNotification
    class SMSAdapter
    class LogDecorator
    class TimestampDecorator

    NotificationFactory --> EmailNotification
    NotificationFactory --> SMSNotification
    NotificationFactory --> PushNotification
    SMSAdapter --> ExternalSMSService
    LogDecorator --> EmailNotification
    TimestampDecorator --> EmailNotification
