from django.urls import path
from .import apiviews

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('polls', apiviews.PollViewSet)
urlpatterns = [
    path('polls/', apiviews.PollList.as_view(), name='polls-list'),
    path('polls/<int:pk>/', apiviews.PollDetail.as_view(), name='polls-detail'),
    path('polls/<int:pk>/choices/', apiviews.ChoiceList.as_view(), name='choice-list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', apiviews.CreateVote.as_view(), name='create-vote'),

    path('users/', apiviews.UserCreate.as_view(), name='user-create'),
    path('login/', apiviews.LoginView.as_view(), name='login')
]

urlpatterns += router.urls