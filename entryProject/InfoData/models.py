from django.db import models

# Create your models here.
RESPONSE_STATUS = (
    ("0", "Not Good"),
    ("1", "Good"),
    ("2", "Perfect"),
)
class InfoModal(models.Model):
    first_name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100, unique=True)
    mobile_number = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    response_status = models.CharField(max_length=20, choices=RESPONSE_STATUS, default='0')