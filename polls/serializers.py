from rest_framework.serializers import ModelSerializer

from polls.models import Poll, Question, Answer, PollResult, Choice


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'poll_id', 'text', 'answer_type')


class PollListItemSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = ('id', 'title', 'description', 'start_date', 'end_date')
        read_only_fields = ('start_date',)


class PollSerializer(ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ('id', 'title', 'description', 'start_date', 'end_date', 'questions')
