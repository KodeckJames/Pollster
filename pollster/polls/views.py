from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Questions, Choices


# Get questions and display them
def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# Show specific question and choices
def detail(request, question_id):
    try:
        question = Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
        raise Http404("Question doesn't exist")
    return render(request, 'polls/detail.html', {'question': question})

# Get question and display results
def results(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# Vote for a question choice
def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choices.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))