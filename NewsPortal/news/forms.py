from django import forms
from .models import Post
from django.core.exceptions import ValidationError
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
class DateInput(forms.DateInput):
    input_type = 'date'
class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = [
            'author',
            'category',
            'head_name',
            'article_text',
        ]

    def clean(self):
        cleaned_data = super().clean()
        article_text = cleaned_data.get("article_text")
        if article_text is not None and len(article_text) < 20:
            raise ValidationError({
                "article_text": "Публикация не может быть менее 20 символов."
            })
        head_name = cleaned_data.get("head_name")
        if head_name == article_text:
            raise ValidationError(
                "Название не должно быть идентично посту."
            )

        return cleaned_data

class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='basic')
        basic_group.user_set.add(user)
        return user