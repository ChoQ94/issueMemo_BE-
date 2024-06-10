from django.db import models
from django.conf import settings
from django.utils import timezone


class Issue(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)

   # 함수 매서드
    def publish(self):
        self.published_at = timezone.now()

    def __str__(self):
        return self.title
