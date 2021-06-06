from rest_framework.serializers import ModelSerializer
from django.db.transaction import atomic

from polls.models import Poll, Question, Answer, PollResult, Choice


class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'question_id', 'text')
        read_only_fields = ('id',)


class QuestionSerializer(ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=False)

    class Meta:
        model = Question
        fields = ('id', 'poll_id', 'text', 'answer_type', 'choices')
        read_only_fields = ('id',)

    def update(self, instance, validated_data):
        with atomic():
            Choice.objects.filter(question=instance).delete()
            new_choices = [Choice(**kwargs) for kwargs in validated_data.get('choices')]
            Choice.objects.bulk_create(new_choices)


class PollListItemSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = ('id', 'title', 'description', 'start_date', 'end_date')
        read_only_fields = ('start_date', 'id')


class PollSerializer(ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ('id', 'title', 'description', 'start_date', 'end_date', 'questions')
        read_only_fields = ('start_date', 'id', 'questions')
