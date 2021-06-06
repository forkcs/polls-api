from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=1000, blank=False, null=False)
    description = models.TextField(blank=True, null=True)

    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)

    updated = models.DateTimeField(auto_now=True)


ANSWER_TYPES = (
    ('text', 'Plain text'),
    ('single_choice', 'Single choice'),
    ('mul_choices', 'Multiple choices')
)


class Question(models.Model):
    poll = models.ForeignKey(to='Poll', blank=False, null=False, on_delete=models.CASCADE, related_name='questions')

    text = models.TextField(blank=False, null=False)
    answer_type = models.CharField(max_length=100, blank=True, null=False, default='text', choices=ANSWER_TYPES)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Choice(models.Model):
    question = models.ForeignKey(to='Question', blank=False, null=False,
                                 on_delete=models.CASCADE, related_name='choices')

    text = models.CharField(max_length=1000, blank=False, null=False)


class PollResult(models.Model):
    poll = models.ForeignKey(to='Poll', blank=False, null=True, on_delete=models.SET_NULL)
    user_uid = models.IntegerField(blank=False, null=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Answer(models.Model):
    question = models.ForeignKey(to='Question', blank=False, null=False, on_delete=models.CASCADE)
    poll_result = models.ForeignKey(to='PollResult', blank=False, null=False, on_delete=models.CASCADE)

    text = models.TextField(blank=True, null=True)
    choices = models.ManyToManyField(to='Choice')
