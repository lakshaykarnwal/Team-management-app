from asyncio import Task
from multiprocessing import context
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Member
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class MemberList(ListView):
    model = Member
    context_object_name = 'members'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['members'] = context['members'].filter(
                first_name__icontains=search_input)

        context['search_input'] = search_input

        return context


class MemberDetail(DetailView):
    model = Member
    context_object_name = 'member'
    template_name = 'base/member.html'


class MemberCreate(CreateView):
    model = Member
    fields = '__all__'
    success_url = reverse_lazy('members')


class MemberUpdate(UpdateView):
    model = Member
    fields = '__all__'
    success_url = reverse_lazy('members')


class DeleteView(DeleteView):
    model = Member
    context_object_name = 'member'
    success_url = reverse_lazy('members')
