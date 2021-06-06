from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from polls.serializers import PollListItemSerializer, PollSerializer, QuestionSerializer
from polls.models import Poll


class PollsListView(ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollListItemSerializer


class PollsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class QuestionsListView(UpdateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        kwargs.setdefault('many', True)
        super(QuestionsListView, self).get_serializer(*args, **kwargs)
