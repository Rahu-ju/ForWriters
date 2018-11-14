from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from .models import Article, Comment, Reply
from .forms import CommentForm


# for article ..
class ArticleListView(ListView):
    '''Display the list of all articles'''
    model = Article
    template_name = 'article_list.html'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'body']
    template_name = 'article_create.html'
    login_url = 'login'

    def form_valid(self, form):
        '''Editing this built in method to automatically fill the author field depends on who is signed in. '''
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ['title', 'body', ]
    template_name = 'article_edit.html'
    login_url = 'login'


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'


# for Comment and comment Reply
class CommentCreateView(CreateView):
    '''Let the user to comment of an article. '''
    model = Comment
    fields = ['comment']
    template_name = 'comment.html'
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article = Article.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)





class ReplyCreateView(CreateView):
    '''Let user to reply of an comment.'''
    model = Reply
    fields = ['reply']
    template_name = 'reply.html'
