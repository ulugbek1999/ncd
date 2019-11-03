from django.db import models

class MailingList(models.Model):
    email = models.CharField(max_length=50, blank=False, null=False)
    country_code = models.CharField(max_length=3, blank=False, null=False)

    class Meta:
        db_table = "mailing_list"
        ordering = ["-id", ]