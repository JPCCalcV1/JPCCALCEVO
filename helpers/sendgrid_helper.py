import os
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
FROM_EMAIL = os.getenv("FROM_EMAIL")

# Sicherstellen, dass die Variablen gesetzt sind
if not SENDGRID_API_KEY:
    raise ValueError("Environment variable 'SENDGRID_API_KEY' is not set!")
if not FROM_EMAIL:
    raise ValueError("Environment variable 'FROM_EMAIL' is not set!")


def send_email(to_email, subject, body_text, body_html=None):
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    from_email = Email(FROM_EMAIL)  # Aus Render-Umgebung laden
    to_email = To(to_email)
    content = Content("text/plain", body_text)
    mail = Mail(from_email, to_email, subject, content)

    if body_html:
        mail.add_content(Content("text/html", body_html))

    response = sg.client.mail.send.post(request_body=mail.get())
    return response.status_code