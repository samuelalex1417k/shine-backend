import requests
from django.conf import settings

def send_email(to_email, subject, html_content):
    response = requests.post(
        "https://api.resend.com/emails",
        headers={
            "Authorization": f"Bearer {settings.RESEND_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "from": "Shine LLC <onboarding@resend.dev>",
            "to": [to_email],
            "subject": subject,
            "html": html_content,
        },
    )

    print(response.status_code, response.text)  # 👈 ADD THIS FOR DEBUG

    return response.status_code