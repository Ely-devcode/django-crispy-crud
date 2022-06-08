
from App.models import Candidate
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
# Create your views here.

#(C) CREATE


class Create(CreateView):
    model = Candidate
    fields = '__all__'
    success_url = reverse_lazy('read')

#(R) READ


class Read(ListView):
    model = Candidate
    queryset = Candidate.objects.all()

#(U) UPDATE


class Update(UpdateView):
    model = Candidate
    fields = '__all__'
    success_url = reverse_lazy('read')

#(D) DELETE
class Delete(DeleteView):
    queryset = Candidate.objects.all()
    success_url = reverse_lazy('read')
