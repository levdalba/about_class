from datetime import datetime


def send_sms(msg, phone):
    """Sends a given message to a given phone via SMS."""
    print(f"SMS sent to {phone}: {msg}")


def send_email(msg, email):
    """Sends a given message to a given address as email."""
    print(f"Email sent to {email}: {msg}")


class Patient:
    def __init__(self, first_name, last_name, title, birthdate, email, phone, mobile):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.birthdate = birthdate
        self.email = email
        self.phone = phone
        self.mobile = mobile

    def calculate_age(self):
        today = datetime.now()
        age = today.year - self.birthdate.year
        months_diff = today.month - self.birthdate.month
        days_diff = today.day - self.birthdate.day

        if days_diff < 0:
            months_diff -= 1
            days_diff += 30

        age_str = f"{age} Y {months_diff} M {days_diff} D"
        return age_str

    def greeting(self):
        return f"Hello, {self.title} {self.first_name} {self.last_name}!"

    def send_appointment_reminder(self, appointment_date):
        age = self.calculate_age()
        message = f"Dear {self.first_name}, your appointment is scheduled on {appointment_date}. You are {age} old."
        send_sms(message, self.mobile)
        send_email(message, self.email)


patient1 = Patient(
    "John",
    "Doe",
    "mr.",
    datetime(1990, 2, 28),
    "john.doe@gmail.com",
    "+3345451555",
    "+6693932030",
)

print(patient1.greeting())

patient1.send_appointment_reminder(datetime(2023, 10, 13, 13, 0))
