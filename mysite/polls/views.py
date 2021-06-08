from django.shortcuts import render
from django.http import HttpResponse
from .models import Choice, Question

# Create your views here.
def index(request):
    name = 'Huy Tung'
    taisan = ['dienthoai', 'maytinh', 'banphim', 'chuot']
    context = {'name':name, 'taisan':taisan}
    
    return render(request, "polls/index.html", context)

def view_db(request):
    list_question = Question.objects.all()
    context = {'list_question':list_question}
    return render(request, 'polls/ls_questions.html', context)

def detail_view(request, qs_id):
    # Get question from question id
    q = Question.objects.get(pk=qs_id)
    context = {'question' : q}
    return render(request, 'polls/qs_detail.html', context)

def votes(request, qs_id):
    q = Question.objects.get(pk=qs_id)
    choice_id = request.POST['choice']
    c = q.choice_set.get(pk=choice_id)
    c.vote = c.vote + 1
    c.save()
    return render(request, 'polls/results.html', {'question' : q})