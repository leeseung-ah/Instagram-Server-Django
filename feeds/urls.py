from django.urls import path
from .views import MyFeed, UserNameFeeds

urlpatterns = [
    path("", MyFeed.as_view()),
    path("<str:username>", UserNameFeeds.as_view())
]