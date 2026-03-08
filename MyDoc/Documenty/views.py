from django.shortcuts import render
from .models import Filials
from .forms import FilialsForm

def messanger(request):
    error = ''
    if request.method == 'POST':
        form = FilialsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'nooooou'

    form = FilialsForm()

    data = {
        'form': form,
        'error': error,
        'filial': Filials
    }
    return render(request, 'Documenty/messanger.html', data)
