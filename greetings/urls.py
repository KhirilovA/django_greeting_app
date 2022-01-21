from django.urls import path
from .views import NamesListView, GreetingView

urlpatterns = [
    path('names_list/', NamesListView.as_view(), name='name-list'),
    path('', GreetingView.as_view(), name='greeting'),
    ]