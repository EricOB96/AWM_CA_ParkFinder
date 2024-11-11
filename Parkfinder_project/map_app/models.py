from django.contrib.gis.db import models


class Park(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    amenities = models.JSONField(default=dict)
    geo = models.PointField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name