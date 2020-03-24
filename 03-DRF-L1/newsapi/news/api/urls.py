from django.urls import path
from news.api.views import ArticleDetailAPIView,ArticleListCreateAPIView,JournalistListCreateAPIView   #Alist_C_APIview,Adetail_C_APIview
urlpatterns = [
    path("articles/", ArticleListCreateAPIView.as_view(), name="article-list"),
    path("articles/<int:pk>/", ArticleDetailAPIView.as_view(), name="article-detail"),
    path("journalists/", JournalistListCreateAPIView.as_view(), name="journalist-list")
    
                    # function based api view
    # path("articles/", Alist_C_APIview, name="article-list"),
    # path("articles/<int:pk>", Adetail_C_APIview, name="article-detail")
]