from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question
from .forms import NewQuestionForm, NewChoiceForm


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list_view'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-question_text')
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1.1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def create_question(request):
	if request.method == 'POST':
		form = NewQuestionForm(request.POST)
		if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('polls:index'))
	else:
			form = NewQuestionForm()

	return render(request, 'polls/create_question.html', {'form': form})

def create_choice(request, question_id):
	question = get_object_or_404(Question, pk=question_id)

	if request.method == 'POST':
		form = NewChoiceForm(request.POST, instance=question)
		if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('polls:index'))
	else:
			form = NewChoiceForm()

	context = {'form':form, 'question':question}
	return render(request, 'polls/create_choice.html', context)
