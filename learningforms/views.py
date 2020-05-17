from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from taggit.models import Tag
# class-based generic views
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# import models
from .forms import ContactForm


############## index view ############## 
def index(request):
    return HttpResponseRedirect(reverse('learningforms:send_message'))



############## send_message views ############## 
class SendMessage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'learningforms/send_message.html', {'form': ContactForm})

    def post(self, request, *args, **kwargs):
        form =  ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponse('Your Message has been sent')

        return render(request, 'learningforms/send_message.html', {'form': form})


"""

class SendMessage(View):
    get(self, re)
    model = Lesson
    template_name = 'lessons/lesson/lesson_list.html'
    context_object_name = 'lesson_list'
    paginate_by = 5

class LessonListByTag(ListView):
    template_name = 'lessons/lesson/lesson_list.html'
    context_object_name = 'lesson_list'
    paginate_by = 5

    def get_queryset(self):
        # filter lessons by self.kwargs['tag_id']
        tag = get_object_or_404(Tag, pk=self.kwargs['tag_id'])
        return Lesson.objects.filter(tags__in=[tag])

class LessonDetail(DetailView):
    model = Lesson
    template_name = 'lessons/lesson/lesson_detail.html'
    context_object_name = 'lesson'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # if pdf_docs is uploaded we add file_uploaded to the context 
        if context['lesson'].pdf_docs:
            context['file_uploaded'] = True 

        return context


class LessonCreate(CreateView):
    model = Lesson
    template_name = 'lessons/lesson/lesson_form_create.html'
    fields = '__all__'
    # fields = ['title', 'description', 'city', 'state_province', 'country', 'website']
    
class LessonUpdate(UpdateView):
    model = Lesson
    template_name = 'lessons/lesson/lesson_form_update.html'
    fields = '__all__'
    # fields = ['name', 'address', 'city', 'state_province', 'country', 'website']
        
class LessonDelete(DeleteView):
    model = Lesson
    template_name = 'lessons/lesson/lesson_confirm_delete.html'
    success_url = reverse_lazy('lessons:lesson-list')



"""
