from __future__ import unicode_literals

from django.db import models

class Landlord(models.Model):
    landlord_name = models.CharField(max_length=100)
    landlord_email = models.CharField(max_length=100, blank=True)
    contact_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    score = models.FloatField(default=0.0)
    address = models.CharField(max_length=100)
    link = models.CharField(max_length=100, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def as_json(self):
        return dict(
            landlord_name=self.landlord_name,
            landlord_email=self.landlord_email,
            contact_name=self.contact_name,
            phone_number=self.phone_number,
            score=self.score,
            address=self.address,
            link=self.link,
            latitude=self.latitude,
            longitude=self.longitude
        )

class Review(models.Model):
    reviewer_name = models.CharField(max_length=100)
    reviewer_email = models.CharField(max_length=100)
    review_text = models.CharField(max_length=1000)
    star_rating = models.FloatField()
    landlord = models.ForeignKey(
        'Landlord',
        on_delete=models.CASCADE
    )

    def as_json(self):
        return dict(
            reviewer_name=self.reviewer_name,
            reviewer_email=self.reviewer_email,
            review_text=self.review_text,
            star_rating=self.star_rating,
            landlord=self.landlord.as_json()
        )
