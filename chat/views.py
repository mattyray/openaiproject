# chat/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm
from .services import get_motivational_response

@login_required
def chat_view(request):
    messages = Message.objects.filter(user=request.user).order_by('timestamp')
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Save user message
            user_message = form.save(commit=False)
            user_message.user = request.user
            user_message.save()

            # Generate AI response
            ai_response = get_motivational_response(user_message.text)
            Message.objects.create(user=request.user, text=ai_response, is_user=False)

            return redirect('chat')

    return render(request, 'chat/chat.html', {'messages': messages, 'form': form})
