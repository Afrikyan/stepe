from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from models import Question
from utils import paginate


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def question_list(request):
    qs = Question.objects.all()
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('main') + '?page='
    context = {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    }
    return render(request, 'list.html', context)


def popular(request):
    qs = Question.objects.all()
    qs = qs.order_by('-rating')
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('popular') + '?page='
    context = {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    }
    return render(request, 'list_rating.html', context)


def question_detail(request, id):
    question = get_object_or_404(Question, id=id)
    answers = question.answer_set.all()
    context = {
        'question': question,
        'answers': answers,
    }
    return render(request, 'detail.html', context)
