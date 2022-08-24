from django.urls import path
from .views import SnackListView, SnackDetailView, SnackDeleteView, SnackCreateView, SnackUpdateView


urlpatterns =[
  path('list/', SnackListView.as_view(), name='snacks_list'),
  path('<int:pk>/', SnackDetailView.as_view(), name='snack_detail'),
  path('delete/', SnackDeleteView.as_view(), name='snack_delete'),
  path('create/', SnackCreateView.as_view(), name='snack_create'),
  path('update/', SnackUpdateView.as_view(), name='snack_update')
]
