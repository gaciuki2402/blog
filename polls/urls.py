from django.urls import path
from polls import views

urlpatterns = [
    path('<int:question_id>/', views.detail, name='detail'),

]