from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from users.models import CustomUser
# from .forms import FilterForm
from django.shortcuts import render # 2022-12-09
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    def get_queryset(self):
        '''Return all news stories.'''
        # previously return NewsStory.objects.all()
        return NewsStory.objects.order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = self.get_queryset()[:4]
        context['all_stories'] = self.get_queryset()
        return context
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    # context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ByAuthorView(generic.ListView):
    template_name = 'news/author.html'
    def get_queryset(self):
        '''Return news stories by specified author.'''
        # previously return NewsStory.objects.all()
        return NewsStory.objects.filter().order_by('-pub_date')

    def get_context_data(self, **kwargs):
        auth_id = self.kwargs['auth_id']
        auth_details = CustomUser.objects.get(id=auth_id)
        auth_queryset = NewsStory.objects.filter(author_id=auth_id).order_by('-pub_date')
        context = super().get_context_data(**kwargs)
        context['author_stories'] = auth_queryset # dictionary
        context['author'] = auth_details
        # print(f"context={context}")
        return context

# 
class StoryEditView(LoginRequiredMixin, generic.UpdateView): # Update expects form
    model = NewsStory
    fields = ['title','pub_date','content']
    
    # Use function to do something dynamic
    def get_success_url(self) -> str:
        return reverse_lazy('news:story', kwargs={"pk":self.kwargs['pk']})
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

class StoryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = NewsStory
    success_url = reverse_lazy('news:index')

    def get_queryset(self):
        """ filter to only allow delete of own stories """
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

