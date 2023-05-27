import django
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


arcticle = 'AR'
news = 'NW'

TYPE = [
    (arcticle, 'Статья'),
    (news, 'Новость')
]


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)

    def update_rating(self):
        author_posts_rating = Post.objects.filter(author_id=self.pk).aggregate(
            post_rating_sum=Coalesce(Sum('rate') * 3, 0))
        author_comment_rating = Comment.objects.filter(user_id=self.user).aggregate(
            comments_rating_sum=Coalesce(Sum('rate'), 0))
        author_post_comment_rating = Comment.objects.filter(post__author__user=self.user).aggregate(
            comments_rating_sum=Coalesce(Sum('rate'), 0))
        print(author_posts_rating)
        print(author_post_comment_rating)
        print(author_post_comment_rating)
        self.rate = author_posts_rating['post_rating_sum'] + author_comment_rating['comments_rating_sum'] \
                    + author_post_comment_rating['comments_rating_sum']
        self.save()

    def __str__(self):
        return self.user.username


class Category(models.Model):

    #category_name = models.CharField(max_length=255, unique=True)

    gossip = 'GS'
    policy = 'PO'
    technology = 'TH'
    bullet = 'BL'

    TEMATIC = [
        (gossip, 'СВЕТСКИЕ НОВОСТИ'),
        (policy, 'ПОЛИТИКА'),
        (technology, 'ТЕХНИКА'),
        (bullet, 'СРОЧНЫЕ НОВОСТИ')
    ]
    thematic = models.CharField(max_length=2, choices=TEMATIC, unique=True,)
    subscribers = models.ManyToManyField(User, blank=True, related_name='categories')

    def __str__(self):
        return self.get_thematic_display()


post = 'PO'
news = 'NE'
POST = [
    (post, 'ПОСТ'),
    (news, 'НОВОСТЬ')
]


class Post(models.Model):

    objects = None
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=TYPE, default='news')
    time_in = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through="PostCategory")
    head_name = models.CharField(max_length=250, unique=True)
    article_text = models.TextField()
    rate = models.IntegerField(default=0)

    def __str__(self):
        return self.head_name

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def like(self):
        self.rate += 1
        self.save()

    def dislike(self):
        self.rate -= 1
        self.save()

    def preview(self):
        article_text = self.article_text
        preview = article_text[0:124]
        points = "..."
        return preview + points

class PostCategory(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)



class Comment(models.Model):
    comment_post = models.ForeignKey('Post', on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_date = models.DateTimeField()
    comment_rating = models.IntegerField(default=0)

    def like(self, amount=1):
        self.comment_rating += amount
        self.save()

    def dislike(self, amount=1):
        self.comment_rating -= amount
        self.save()


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2",)


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='basic')
        basic_group.user_set.add(user)
        return user