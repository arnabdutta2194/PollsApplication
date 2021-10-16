from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, response,Http404, HttpResponseRedirect
from .models import Question,Choice
from django.template import loader
from django.urls import reverse
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # template = loader.get_template('polls/index.html')
    # context = { 'latest_question_list' : latest_question_list}
    # return HttpResponse(template.render(context, request))

    context = { 'latest_question_list' : latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request,question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question Does Not Exists')
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})


def results(request, question_id):
    # response = "You are looking at the result of question %s"
    # return HttpResponse(response % question_id)

    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
    # return HttpResponse("You are voting on question %s." % question_id)

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html' , {
            'question' : question_id,
            'error_message' : "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) #To Prevent Data from being posted twice
    

def owner(request):
    return HttpResponse("Hello, World 816a6db4 is the polls index")