import secrets
from django.db import models

#Account model
class Account(models.Model):
  account_name = models.CharField(max_length=50)
  email_id = models.EmailField(unique=True)
  app_secret_token = models.CharField(max_length=32, unique=True, blank=True)
  website = models.URLField(null=True, blank=True)
  #creating a unique whenever the account is saved
  def save(self, *args, **kwargs):
    if not self.app_secret_token:
      self.app_secret_token = secrets.token_hex(32)

    super().save(*args, **kwargs)

  def __str__(self):
    return self.account_name

#Destination Model
class Destination(models.Model):
  account = models.ForeignKey(Account, related_name='destinations',on_delete=models.CASCADE)
  destination_url = models.URLField()
  http_method = models.CharField(max_length=10)
  header = models.JSONField()