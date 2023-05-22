from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from accounts.models import Deposit, User
from .TokenGenerator import generateToken
from django.urls import reverse
import threading


def generateSecureEmailCredentials(user):
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    token = generateToken.make_token(user)

    return {"uidb64": uidb64, "token": token}


class SendEmail:
    def __init__(self, template, subject, to) -> None:
        self.template = template
        self.subject = subject
        self.to = to
        self.send()

    def send(self):
        self.sendEmailNow(),

    def sendEmailNow(self):
        e = EmailMultiAlternatives(
            subject=self.subject,
            body=strip_tags(self.template),
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=self.to,
        )
        e.attach_alternative(self.template, "text/html")
        e.send()


def send_activation_email(user, request, template, urlPath, subject):
    email = user.email
    user = User.objects.get(email=email)

    template = render_to_string(template, {"urlPath": urlPath, "user": user})

    s = SendEmail(template=template, subject=subject, to=(user.email,))


def actionNotificationEmail(message, to, title=""):
    template = render_to_string(
        "emails/action_notification.html", {"message": message, "title": title}
    )
    

    s = SendEmail(template=template, subject="Action Notification", to=(to,))


def generateUserReferalLink(request, user):
    domain = get_current_site(request).domain
    path = reverse("register")
    return f"{domain}{path}?username={user.username}&referal_code={user.referal.code}"

def referalActivities(refering_user, refered_user,request,deposit_amount, is_new=False):
    domain = "https://"+get_current_site(request).domain
    path = reverse("referal")
    referalLink = f"{domain}{path}"

    d = Deposit.objects.create(
                amount = deposit_amount,
                currency_type="REFERAL DEPOSIT",
                wallet = "__",
                user = refering_user,
                status=True,
                is_referal =True

            )

    if not is_new:
        message_referal =f'''
        <center><p style='color:green;font-size:1.4em;'>Optima Investment</p></center>
        Hello investor {refering_user.username},<br />
        congratulations, you have recieved a referal commission of {deposit_amount} USD.<br />
        from {refered_user.username}'s investment<br />
        Your balance is {refering_user.getUserBalance} USD.
        <center><a href={referalLink}>Check your Referal Details</a></center>
        
        '''
    else:
        message_referal =f'''
            <center><p style='color:green;font-size:1.4em;'>Optima Investment</p></center>
            Hello investor {refering_user.username},<br />
            congratulations, you have recieved a referal commission of {deposit_amount} USD.<br />
            from {refered_user.username}'s successful account creation<br />
            Your balance is {refering_user.getUserBalance} USD.
            You will also recieve 5% of {refered_user.username}'s future Deposits.
            <center><a href={referalLink}>Check your Referal Details</a></center>
            
            '''



   

    
    
    

    
    t = threading.Thread(target=actionNotificationEmail, kwargs={"message":message_referal,"to":refering_user.email, "title":"Referal Notification."})
    t.start()


