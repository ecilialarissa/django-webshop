from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from.models import *

class MyListView(ListView):
    template_name = 'produtolista.html'
    queryset = Produto.objects.all() 

class HomeView(TemplateView): 
    template_name = "home.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['produto_list'] = Produto.objects.all()
        return context 

class SobreView(TemplateView): 
    template_name = "sobre.html" 

class ContatoView(TemplateView): 
    template_name = "contato.html" 


# Create your views here.
