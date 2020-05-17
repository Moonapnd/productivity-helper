from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from taggit.models import Tag
# class-based generic views
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# import models
from .models import Miniproject


############## Miniprojects index ##############
def index(request):
    return HttpResponseRedirect(reverse('miniprojects:miniproject-list'))



############## Miniprojects views ##############
class MiniprojectList(ListView):
    model = Miniproject
    template_name = 'miniprojects/miniproject/miniproject_list.html'
    context_object_name = 'miniproject_list'
    paginate_by = 5

class MiniprojectListByTag(ListView):
    template_name = 'miniprojects/miniproject/miniproject_list.html'
    context_object_name = 'miniproject_list'
    paginate_by = 5

    def get_queryset(self):
        # filter miniprojects by self.kwargs['tag_id']
        tag = get_object_or_404(Tag, pk=self.kwargs['tag_id'])
        return Miniproject.objects.filter(tags__in=[tag])

class MiniprojectDetail(DetailView):
    model = Miniproject
    template_name = 'miniprojects/miniproject/miniproject_detail.html'
    context_object_name = 'miniproject'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # if pdf_docs is uploaded we add file_uploaded to the context
        if context['miniproject'].pdf_docs:
            context['file_uploaded'] = True

        return context


class MiniprojectCreate(CreateView):
    model = Miniproject
    template_name = 'miniprojects/miniproject/miniproject_form_create.html'
    fields = '__all__'
    # fields = ['title', 'description', 'city', 'state_province', 'country', 'website']

class MiniprojectUpdate(UpdateView):
    model = Miniproject
    template_name = 'miniprojects/miniproject/miniproject_form_update.html'
    fields = '__all__'
    # fields = ['name', 'address', 'city', 'state_province', 'country', 'website']

class MiniprojectDelete(DeleteView):
    model = Miniproject
    template_name = 'miniprojects/miniproject/miniproject_confirm_delete.html'
    success_url = reverse_lazy('miniprojects:miniproject-list')


