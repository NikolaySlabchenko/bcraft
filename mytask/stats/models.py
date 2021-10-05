from django.db import models


class Stats(models.Model):
    date = models.DateTimeField(blank=True, verbose_name='Дата')
    views = models.IntegerField(blank=True, verbose_name='Просмотры')
    clicks = models.IntegerField(blank=True, verbose_name='Клики')
    cost = models.FloatField(max_length=999999.99, verbose_name='Цена')
    cpc = models.FloatField(editable=False)
    cpm = models.FloatField(editable=False)

    def save(self, *args, **kwargs):
        self.cost = round(self.cost, 2)
        self.cpc = self.cost/self.clicks
        self.cpm = self.cost/self.views * 1000
        super(Stats, self).save(*args, **kwargs)
