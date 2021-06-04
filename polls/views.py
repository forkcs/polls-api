from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from polls.serializers import PollListItemSerializer, PollSerializer
from polls.models import Poll


class PollsListView(ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollListItemSerializer


class PollsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
