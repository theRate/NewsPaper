from django.views.generic import ListView, DetailView

from .models import Post


# Create your views here.
class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')


class NewsDetail(DetailView):
    model = Post
    template_name = 'det_news.html'
    context_object_name = 'det_news'
