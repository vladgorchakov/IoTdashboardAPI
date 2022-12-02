from django.db import models


class DataTimeModelMixin(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TitleDescriptionModelMixin(models.Model):
    title = models.CharField(max_length=25, unique=True)
    description = models.TextField(max_length=1000, blank=True, null=True)

    class Meta:
        abstract = True


class Measure(TitleDescriptionModelMixin, DataTimeModelMixin):
    def __str__(self):
        return f'{self.title}'
