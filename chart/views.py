from rest_framework import permissions
from rest_framework import mixins, viewsets
from datetime import datetime
from django.utils.timezone import make_aware

from .serializers import OhlcSerialiser
from .models import CandleStick

class ChartsListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = CandleStick.objects.all()
    serializer_class = OhlcSerialiser
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        startime = make_aware(datetime.fromtimestamp(int(self.request.GET['startime'])))
        endtime = make_aware(datetime.fromtimestamp(int(self.request.GET['endtime'])))
        queryset = CandleStick.objects.filter(ticker=self.kwargs.get('ticker'), timestamp__range=[startime, endtime]).all()
        
        return queryset

