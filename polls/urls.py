from django.urls import path
from django.urls.conf import include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
# router.register(r'groups', views.GroupViewSet)

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('api/', include(router.urls)),
    # path('api/questions/<int:pk>', views.CustomQuestionViewSet.as_view()),
]
