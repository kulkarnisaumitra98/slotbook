from django.db import models


class Register(models.Model):
    # field_field = models.TextField(blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    college = models.TextField(blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    date = models.TextField( blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'. This field type is a guess.
    email1 = models.EmailField(blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    email2 = models.EmailField(blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    events = models.TextField(blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    field_id = models.TextField(blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    name1 = models.TextField(blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    name2 = models.TextField( blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    name3 = models.TextField(blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    name4 = models.TextField( blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    phone1 = models.TextField( blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    phone2 = models.TextField(blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    receipt_no = models.TextField(blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    total = models.TextField(blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    year = models.TextField(blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    session = models.TextField(default="true")

    def __str__(self):

        return self.receipt_no


class SlotsTiming(models.Model):
    time_slot = models.TextField(null=True, blank=True)


class Booking(models.Model):
    user = models.TextField(null=True, blank=True)  # reg_id//receipt_no
    clash = models.TextField(null=True, blank=True)
    rc = models.TextField(null=True, blank=True)
    enigma = models.TextField(null=True, blank=True)
    c_day = models.TextField(null=True, blank=True)
    r_day = models.TextField(null=True, blank=True)
    e_day = models.TextField(null=True, blank=True)
    email_response = models.TextField(default="",null=True, blank=True)

    def __str__(self):

        return self.user