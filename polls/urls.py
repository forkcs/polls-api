from django.urls import path

from polls import views


urlpatterns = [
    path('polls/', views.PollsListView.as_view(), name='polls-list'),
    path('polls/<int:pk>/', views.PollsDetailView.as_view(), name='polls-detail'),

    path('polls/<int:pk>/questions/', views.QuestionsListView.as_view(), name='questions-list'),
    # path('polls/<int:pk>/result/', views.ResultCreateView.as_view(), name='result-create'),
]
