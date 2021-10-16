from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    ### ---  Function Implementation of Views URLS --- ###
    # path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),

    ### ---  Class Implementation of Views URLS --- ###
    path('',views.IndexView.as_view(), name ='index'),
    path('<int:question_id>/', views.DetailView.as_view(), name = 'detail'),
    path('<int:question_id>/results', views.ResultsView.as_view(), name = 'results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('owner', views.owner, name='owner'), #Assignment Section
]