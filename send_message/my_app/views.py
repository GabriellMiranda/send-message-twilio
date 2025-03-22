from django.shortcuts import render
from .forms import MessageForm
from .utils import send_message_via_whatsapp 
import os
from django.conf import settings

def send_message(request):
    if request.method == 'POST':
        print(request)
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            whatsapp_number = form.cleaned_data['whatsapp_number']

            send_message_via_whatsapp(message, whatsapp_number)

            return render(request, 'success.html', {'message': 'Mensagem enviada com sucesso!'})
    else:
        form = MessageForm()

    return render(request, 'send_message.html', {'form': form})
