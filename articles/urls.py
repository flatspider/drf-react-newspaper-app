from django.urls import path

from . import views

# Do I need to create another view for the channels list? What would that return?

urlpatterns = [

    path('', views.ArticleListAPIView.as_view()),
]
