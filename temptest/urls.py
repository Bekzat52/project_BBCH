from django.urls import path, include
from .views import TemlateView

urlpatterns = [
    path('user/', TemlateView.as_view()),
]

# settings допиши