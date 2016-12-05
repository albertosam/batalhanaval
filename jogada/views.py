from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.forms import ModelForm

from jogada.models import Jogada
from jogo.batalha import BatalhaNaval

class JogadaForm(ModelForm):
    class Meta:
        model = Jogada
        fields = ['jogo', 'autor', 'adversario', 'linha', 'coluna', 'acerto']

def jogada_list(request, template_name='jogada/jogada_list.html'):
    jogada = Jogada.objects.all()
    data = {}
    data['object_list'] = jogada
    return render(request, template_name, data)

def jogada_create(request, template_name='jogada/jogada_form.html'):
    form = JogadaForm(request.POST or None)    
    if form.is_valid():
        form.registro = timezone.now()        
        jogada = form.save()

        BatalhaNaval().atualizar(jogada)

        return redirect('jogada:jogada_list')
    return render(request, template_name, {'form':form})

def jogada_update(request, pk, template_name='jogada/jogada_form.html'):
    jogada= get_object_or_404(Jogada, pk=pk)
    form = JogadaForm(request.POST or None, instance=jogada)
    if form.is_valid():
        form.save()
        return redirect('jogada:jogada_list')
    return render(request, template_name, {'form':form})

def jogada_delete(request, pk, template_name='jogada/jogada_confirm_delete.html'):
    jogada= get_object_or_404(Jogada, pk=pk)    
    if request.method=='POST':
        jogada.delete()
        return redirect('jogada:jogada_list')
    return render(request, template_name, {'object':jogada})
