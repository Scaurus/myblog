from django.forms import ModelForm
from blog.models import Comments
from django import forms



class CommentForm(ModelForm):
    class Meta:
        model = Comments
        # fields = '__all__'
        fields = ['comments_text']
        # exclude = ['comments_article_id']