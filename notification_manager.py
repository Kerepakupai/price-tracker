import smtplib
from config import EMAIL_ACCOUNT, EMAIL_PASSWORD


MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"

print(EMAIL_ACCOUNT)

class NotificationManager:
    @staticmethod
    def send_email(email, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as conn:
            conn.starttls()
            conn.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
            conn.sendmail(
                from_addr=EMAIL_ACCOUNT,
                to_addrs=email,
                msg=message
            )
