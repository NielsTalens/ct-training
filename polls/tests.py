from django.test import TestCase
from django.urls import reverse

from .models import Question

class QuestionModelTest(TestCase):
  def too_many_characters_in_the_question_text(self):
    text = "A conventional place for an application’s tests is in the application’s tests.py file; the testing system will automatically find tests in any file whose name begins with test."

    too_long_question = Question(question_text=text)
    self.assertContains(response, "A conventional place for an application’s tests is in the application’s tests.py file; the testing system will automatically find tests in any file whose name begins with test.")
