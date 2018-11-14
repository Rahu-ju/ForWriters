from django.views.generic import ListView
from articles.models import Article


class HomePageView(ListView):
    model = Article
    template_name = 'home.html'
