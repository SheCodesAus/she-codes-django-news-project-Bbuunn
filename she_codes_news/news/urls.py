from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('<int:pk>/edit/', views.StoryEditView.as_view(), name='storyEdit'),
    path('<int:pk>/delete/', views.StoryDeleteView.as_view(), name='storyDelete'),
    path('add-story/', views.AddStoryView.as_view(), name='addStory'),
    path('by-author/<int:auth_id>', views.ByAuthorView.as_view(), name='byAuthor'),
]

urlpatterns += staticfiles_urlpatterns()