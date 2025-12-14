"""Observer Pattern - Define a one-to-many dependency so that when one object changes state, all dependents are notified."""

from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    """Abstract observer interface."""
    
    @abstractmethod
    def update(self, subject: 'Subject'):
        """Receive update from subject."""
        pass


class Subject:
    """Subject that notifies observers of state changes."""
    
    def __init__(self):
        self._observers: List[Observer] = []
        self._state = None
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        self._state = value
        self.notify_observers()
    
    def attach(self, observer: Observer):
        """Attach an observer."""
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer: Observer):
        """Detach an observer."""
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify_observers(self):
        """Notify all observers about state change."""
        for observer in self._observers:
            observer.update(self)


class EmailNotifier(Observer):
    """Concrete observer that sends email notifications."""
    
    def __init__(self, email: str):
        self.email = email
    
    def update(self, subject: Subject):
        print(f"Email to {self.email}: State changed to {subject.state}")


class SMSNotifier(Observer):
    """Concrete observer that sends SMS notifications."""
    
    def __init__(self, phone: str):
        self.phone = phone
    
    def update(self, subject: Subject):
        print(f"SMS to {self.phone}: State changed to {subject.state}")


class LogNotifier(Observer):
    """Concrete observer that logs state changes."""
    
    def update(self, subject: Subject):
        print(f"Log: State changed to {subject.state}")


# Demonstration
if __name__ == "__main__":
    subject = Subject()
    
    email_notifier = EmailNotifier("user@example.com")
    sms_notifier = SMSNotifier("+1234567890")
    log_notifier = LogNotifier()
    
    subject.attach(email_notifier)
    subject.attach(sms_notifier)
    subject.attach(log_notifier)
    
    print("Setting state to 'Active':")
    subject.state = "Active"
    
    print("\nSetting state to 'Inactive':")
    subject.state = "Inactive"
    
    print("\nDetaching SMS notifier:")
    subject.detach(sms_notifier)
    
    print("Setting state to 'Processing':")
    subject.state = "Processing"
