from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.shortcuts import render # 2022-12-09


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
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


