from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'image_url', 'content']
        widgets = {
            'pub_date': forms.DateInput(
                format = ('%m/%d/%Y'),
                attrs = {'class':'form-control',
                'placeholder':'Select a date',
                'type':'date'}
                ),
            }

# ORDER_CHOICE = (
#     ("", "newest first"),
#     ("oldfirst", "oldest first"),
# )
# class FilterForm(forms.Form):
#     order = forms.ChoiceField(label="order", choices=ORDER_CHOICE, required=False)
#     author = forms.ChoiceField(label="author", choices=ORDER_CHOICE, required=False)
#     search = forms.CharField(label="search", required=False)