from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User  # it is for the UserPostListView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from blog.models import Post
from django.urls import reverse_lazy


# def home(request):
#     context = {'posts': Post.objects.all()}
#     return render(request, 'home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']  # to bring the recent post at the top
    paginate_by = 3  # it is used for pagination


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        # we query to db for username, if username doesnot exits then will return 404 error instead of blank page
        user = get_object_or_404(User, username=self.kwargs.get(
            'username'))  # getting username from url
        # it will return the post with the particular user that we get from url
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = "blog/post_form.html"

    # as author is required while submitting form so we want the current user to be the author of the post
    def form_valid(self, form):
        form.instance.author = self.request.user  # means current user is the author
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

# this is to test that the post author can only delete his/her but not other's post (i.e UserPassestestMixin)
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False


def about(request):
    return render(request, 'about.html', {'title': 'About'})
