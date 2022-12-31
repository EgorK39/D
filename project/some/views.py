from pprint import pprint

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import (
    PostModel, Comment, UserModel, User
)
from .forms import PostForm, CommentForm
from .filter import PostFilter

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class Posts(ListView):
    model = PostModel
    ordering = '-time_in'
    template_name = 'views_sites/posts.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['user_name'] = self.request.user.username
        return context


class Post(DetailView):
    model = PostModel
    template_name = 'views_sites/post.html'
    context_object_name = 'post'


class PostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = PostModel
    template_name = 'views_sites/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = PostModel
    template_name = 'views_sites/post_create.html'


@login_required
def post_comment(request, pk):
    post = get_object_or_404(PostModel, id=pk)
    comment = Comment.objects.filter(post=post)
    # form = CommentPost()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comm = form.save(commit=False)

            comm.user = request.user
            comm.post = post
            form.save()
    else:
        form = CommentForm()
    return render(request, 'views_sites/post_comment.html',
                  {'form': form, 'post': post, 'comment': comment})


class MyCommets(LoginRequiredMixin, ListView):
    model = Comment
    ordering = '-time_in'
    template_name = 'views_sites/comments.html'
    context_object_name = 'comments'
    paginate_by = 10

    def get_queryset(self):
        self.user = get_object_or_404(User, username=self.request.user)
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return Comment.objects.filter(user=self.user) and self.filterset.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        context['filterset'] = self.filterset
        pprint(context)
        return context


class MyCommentDetail(LoginRequiredMixin, DetailView):
    model = Comment
    template_name = 'views_sites/comment.html'
    context_object_name = 'comment'


class MyCommentsDelete(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'views_sites/delete.html'
    success_url = reverse_lazy('posts:posts')
    context_object_name = 'postdelete'
