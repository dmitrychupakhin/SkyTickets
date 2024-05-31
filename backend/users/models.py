from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django_rest_passwordreset.signals import reset_password_token_created
from django.dispatch import receiver
from directions.models import *

class User(AbstractUser):
    photo = models.ImageField(upload_to="users", blank=True, null=True, verbose_name='Фотография', default='users/none.jpg')
    email = models.EmailField(blank=False, unique=True)
    phone_number = models.CharField(blank=True, null=True, max_length=20)
    date_birth = models.DateField(blank=True, null=True)
    location = models.CharField(blank=True, null=True, max_length=40)
    
    def save(self, *args, **kwargs):
        if not self.is_superuser and not self.pk:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
        
class favorite_places(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    place = models.ForeignKey(PopularPlace, on_delete=models.CASCADE, blank=False)
    
@receiver(reset_password_token_created)
def password_reser_token_created(reset_password_token, *args, **kwargs):
    sitelink = "http://localhost:8000/"
    token = "&token={}".format(reset_password_token.key)
    ful_link = str(sitelink)+str("password-reset")+str(token)
    
    print(token)
    print(ful_link)
    
    full_link = ful_link,
    recipient_email = reset_password_token.user.email
    
    sender_email = "pikalovshop@yandex.ru"
    subject = "Запрос на сброс пароля"
    message = f"Сброс пароля: {reset_password_token.key}"
    send_mail(subject, message, sender_email, [recipient_email])
