from django.urls import path
from .views import NewsList, NewsDetail, SearchList, PostCreateView, PostDeleteView, PostUpdateView

urlpatterns = [
    path('', NewsList.as_view(), name='news'),
    path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('search', SearchList.as_view(), name='search'),
    path('add', PostCreateView.as_view(), name='add_post'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
]
