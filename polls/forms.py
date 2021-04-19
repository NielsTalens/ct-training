from django import forms
from .models import Question, Choice


# creating a form
class NewQuestionForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Question

        # specify fields to be used
        fields = [
            "question_text",
        ]
class NewChoiceForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    question = kwargs.pop('question')
    super(NewChoiceForm, self).__init__(*args, **kwargs)
    self.fields['question'].initial = question
    print(question.id)
  class Meta:
      # specify model to be used
      model = Choice
      # specify fields to be used
      fields = [
          "question",
          "choice_text",
      ]