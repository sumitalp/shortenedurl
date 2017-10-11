from django.db import models

class ShortenedUrl(models.Model):
	hash_url = models.URLField(max_length=200)
	original_url = models.URLField(max_length=512)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	last_visited_date = models.DateField(blank=True, null=True, )
