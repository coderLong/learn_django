# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Poll, Choice
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404

def index(request):

    latest_question_list = Poll.objects.order_by('-pub_date')[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list":latest_question_list,
    }
    # out_put = ' '.join([q.question for q in latest_question_list])
    return HttpResponse(render(request,'polls/index.html',context))


def detail(request,question_id):
    try:
        question = Poll.objects.get(pk=question_id)
    except Poll.DoesNotExist:
        raise  Http404("question does not exists")
    return render(request,'polls/detail.html',{'question':question})

def vote(request, question_id):
    question = get_object_or_404(Poll, pk=question_id)
    print "request data",request.POST
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 重新显示该问题的表单
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 始终在成功处理 POST 数据后返回一个 HttpResponseRedirect ，
        # （合并上句） 这样可以防止用户点击“后退”按钮时数据被发送两次。
        # （合并至上一句）
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request):
    return request
