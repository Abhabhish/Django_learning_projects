import datetime

from django.test import TestCase
from django.utils import timezone
from .models import Question
from django.urls import reverse

class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now()+datetime.timedelta(seconds=1)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1,seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(),False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now()-datetime.timedelta(hours=23,minutes=59,seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(),True)


def create_question(question_text,days):
    time=timezone.now() + datetime.timedelta(days)
    return Question.objects.create(question_text=question_text,pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_question(self):
        response=self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"],[])

    def test_past_question(self):
        past_question=create_question("past question",-30)
        response=self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"],[past_question])

    def test_future_question(self):
        future_question=create_question("future_question",30)
        response=self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'],[])
    
    def test_future_and_past_question(self):
        past_question=create_question("past_question",-30)
        future_question=create_question("future_question",30)
        response=self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'],[past_question])


class QuestionDetailViewTests(TestCase):
    def test_past_question(self):
        past_question=create_question("past_question",-30)
        url=reverse("polls:detail",args=(past_question.id,))
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,past_question.question_text)

    def test_future_question(self):
        future_question=create_question("future_question",30)
        url=reverse("polls:detail",args=(future_question.id,))
        response=self.client.get(url)
        self.assertEqual(response.status_code,404)
        