from multiprocessing import context
from turtle import title
from unicodedata import name
from django.shortcuts import render, HttpResponseRedirect
from .models import job_post
from django.views import generic

from django.shortcuts import render
from .models import job_post
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


class JobList(generic.ListView):
    def get(self, request, format=None):
        var = job_post.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(var, 2)
        try:
            var1 = paginator.page(page)
        except PageNotAnInteger:
            var1 = paginator.page(1)
        except EmptyPage:
            var1 = paginator.page(paginator.num_pages)
        return render(request, 'home.html', {"var": var1})


class JobDetail(generic.DetailView):
    model = job_post
    template_name = 'job_detail.html'

    '''def get_context_data(request, id):
        # Call the base implementation first to get a context
        context = super().get_context_data(id)
        # Add in a QuerySet of all the books
        context['id', 'title', 'description', ] = job_post.objects.all()
        return context
        '''

    def get(self, request, pk):
        x = job_post.objects.get(id=pk)
        #fm = job_post(instance=x)
        return render(request, 'job_detail.html', {"fm": x})


class JobSearch(generic.ListView):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")

        var = job_post.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

        context = {
            'var': var
        }

        return render(request, 'home.html', context)
