from django.forms import ModelForm
from .models import Comment


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields =['comment', 'author']

    def form_valid(self, form):
        '''Editing this built in method to automatically fill the author field depends on who is signed in. '''
        form.instance.author = self.request.user
        #form.instance.article = self.title
        # article = Article.objects.get(id=5)
        # form.instance.article = article.title

        return super().form_valid(form)
