from django.db import models

# Create your models here.
class Prompt(models.Model):
    """
    Models a prompt template for AP CSA Hackathon 1. Students
    provide a format, style, and subject and the backend
    queries GPT to create a {format} in the style of {style} on the subject of {subject}
    """
    format = models.CharField(max_length=200)
    style = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)