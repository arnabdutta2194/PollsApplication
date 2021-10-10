from django.http import HttpResponse,Http404
from .models import Question
from django.template import loader
from django.shortcuts import render,get_object_or_404


def index(request):
    #### Displaying Some Random Text ####
    # return HttpResponse("Hello, world. You're at the polls index.")

    #### Displaying Static Data Returned from Browser ####
    '''
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
    '''
    #### Using Templates ####
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    ### Displaying Random Text
    # return HttpResponse("You're looking at question %s." % question_id)

    ### Using Http404 Custom Exception
    '''
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    '''
    
    ### ShortCut Method to above function
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)