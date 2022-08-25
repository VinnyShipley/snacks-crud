from django.urls import path
from .views import SnackListView, SnackDetailView, SnackDeleteView, SnackCreateView, SnackUpdateView


urlpatterns =[
  path('', SnackListView.as_view(), name='snacks_list'),
  path('detail/<int:pk>/', SnackDetailView.as_view(), name='snack_detail'),
  path('delete/<int:pk>/', SnackDeleteView.as_view(), name='snack_delete'),
  path('create/', SnackCreateView.as_view(), name='snack_create'),
  path('update/<int:pk>/', SnackUpdateView.as_view(), name='snack_update')
]
