from rest_framework import serializers

from chart import models


class OhlcSerialiser(serializers.ModelSerializer):
   class Meta:
       model = models.CandleStick
       fields = ['id', 'ticker', 'timestamp', 'open_price', 'high_price', 'low_price', 'close_price']