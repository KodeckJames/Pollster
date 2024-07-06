from django.shortcuts import render
from .models import Questions, Choices

# Get questions and display them
def index(request):
    return render(request, 'polls/index.html')
