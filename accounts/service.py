from threading import Thread
from random import randint
from django.core.mail.message import EmailMultiAlternatives

from accounts.utils import generate_code


def send_congratulations_email(receiver_email, first_name):
    subject = 'Congratulations on Your Registration 🎉'

    text_content = f'''
    Hello {first_name},

    Congratulations on successfully registering with us!

    We're thrilled to welcome you to our community. Explore our platform and enjoy the exclusive benefits waiting for you.

    If you have any questions, feel free to reach out to our support team.

    Warm regards,
    Your Company Team
    '''

    from_email = 'vbahodir00@gmail.com'
    to = [receiver_email]

    html_content = f"""
        <div style="font-family: 'Helvetica Neue', Arial, sans-serif; background: #e0f7fa; padding: 40px 20px;">
          <div style="max-width: 600px; margin: auto; background: #ffffff; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
            <!-- Header -->
            <div style="background: linear-gradient(135deg, #ff4081, #f50057); padding: 20px; text-align: center;">
              <h1 style="color: #fff; margin: 0; font-size: 32px;">Congratulations! 🎉</h1>
            </div>
            <!-- Main Content -->
            <div style="padding: 30px; text-align: center;">
              <p style="color: #333; font-size: 18px; margin-bottom: 20px;">
                Hello {first_name}, welcome to our community!
              </p>
              <p style="color: #555; font-size: 16px; margin-bottom: 30px;">
                Your registration was successful. We are excited to have you with us. Dive in and explore the exclusive benefits we offer.
              </p>
              <a href="http://127.0.0.1:8000/" style="background: linear-gradient(135deg, #ff4081, #f50057); color: #fff; padding: 15px 30px; border-radius: 5px; text-decoration: none; font-size: 16px;">
                Get Started
              </a>
            </div>
            <!-- Footer -->
            <div style="background: #f1f1f1; padding: 15px 20px; text-align: center;">
              <p style="color: #888; font-size: 12px; margin: 0;">
                If you have any questions, feel free to <a href="mailto:support@yourcompany.com" style="color: #f50057; text-decoration: none;">contact our support team</a>.
              </p>
              <p style="color: #888; font-size: 12px; margin: 5px 0 0;">
                Best regards,<br>
                <strong>Your Company Team</strong>
              </p>
            </div>
          </div>
        </div>
        """

    email = EmailMultiAlternatives(subject, text_content, from_email, to)
    email.attach_alternative(html_content, 'text/html')

    thread1 = Thread(target=email.send)
    thread1.start()


def forget_password(to_email, user):
    reset_link = 'http://127.0.0.1:8000/accounts/verify_code/'
    subject = f"Hello {user.username}"
    from_email = "khurshid.khbek@gmail.com"
    to = [to_email]
    text_content = "You Forgot the Password"
    html_content = f"""
        <h1> Verification code is: {generate_code(user)} </h1>
        <h3> This is account recovery link: {reset_link}</h3>
        """

    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=from_email,
        to=to,
    )

    email.attach_alternative(html_content, "text/html")
    email.send()


def send_verification_email_async(to_email, user):
    thread1 = Thread(target=forget_password, args=(to_email, user))
    thread1.start()
