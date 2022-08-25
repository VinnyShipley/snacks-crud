from .models import Snack
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse



class SnackListView(ListView):
  template_name = 'snack_list.html'
  model = Snack
  
class SnackDetailView(DetailView):
  template_name = 'snack_detail.html'
  model = Snack
  
class SnackCreateView(CreateView):
  template_name = 'snack_create.html'
  model = Snack
  fields = ['title', 'purchaser', 'description']

  
  
class SnackUpdateView(UpdateView):
  template_name = 'snack_update.html'
  model = Snack
  
class SnackDeleteView(DeleteView):
  template_name = 'snack_delete.html'
  model = Snack
  success_url = reverse_lazy('snacks_list')

