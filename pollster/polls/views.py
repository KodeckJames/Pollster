from django.shortcuts import render
from .models import Questions, Choices

# Get questions and display them
def index(request):
    latext_question_list = Questions.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html')
