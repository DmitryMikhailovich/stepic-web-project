from django.core.paginator import Paginator, EmptyPage
from django.http.response import Http404
from django.shortcuts import render


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    paginator.baseurl = request.path + '?page='
    try:
        page = paginator.page(page)
        paginator.page
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page


def render_question_list(request, ql):
    page = paginate(request, ql)
    return render(request, 'question_list.html', {
        'questions': ql,
        'page': page,
    })