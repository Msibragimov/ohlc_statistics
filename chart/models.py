from django.db import models
from uuid import uuid4


class CandleStick(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    ticker = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    open_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    close_price = models.FloatField()

    def __str__(self):
        return f"{self.ticker} -- {self.timestamp}" 

    class Meta:
        db_table = 'candlestick'