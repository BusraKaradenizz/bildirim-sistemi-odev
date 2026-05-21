classDiagram

&#x20;   class NotificationFactory

&#x20;   class EmailNotification

&#x20;   class SMSNotification

&#x20;   class PushNotification

&#x20;   class SMSAdapter

&#x20;   class LogDecorator

&#x20;   class TimestampDecorator



&#x20;   NotificationFactory --> EmailNotification

&#x20;   NotificationFactory --> SMSNotification

&#x20;   NotificationFactory --> PushNotification

&#x20;   SMSAdapter --> ExternalSMSService

&#x20;   LogDecorator --> EmailNotification

&#x20;   TimestampDecorator --> EmailNotification



