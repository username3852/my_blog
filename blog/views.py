from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
