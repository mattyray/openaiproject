from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Conversation, Message
from .services import get_motivational_response

from .forms import MessageForm  # <-- Make sure to import the form

# chat/views.py

@login_required
def clear_chat(request):
    """Clear the current user's latest chat conversation."""
    conversation_id = request.session.get('conversation_id')
    if conversation_id:
        Conversation.objects.filter(id=conversation_id, user=request.user).delete()
        del request.session['conversation_id']
    return redirect('chat')


@login_required
def chat_view(request):
    """Chat view where users can send messages and receive AI responses."""
    conversation, created = Conversation.objects.get_or_create(user=request.user, id=request.session.get('conversation_id'))
    if created:
        request.session['conversation_id'] = conversation.id

    messages = conversation.messages.order_by('timestamp')
    form = MessageForm()  # <-- Initialize the form

    if request.method == 'POST':
        form = MessageForm(request.POST)  # Bind the form with POST data
        if form.is_valid():  # <-- Check if form is valid
            user_message = Message.objects.create(
                user=request.user,
                conversation=conversation,
                text=form.cleaned_data['text'],
                is_user=True
            )
            ai_response = get_motivational_response(user_message.text)
            Message.objects.create(user=request.user, conversation=conversation, text=ai_response, is_user=False)
            return redirect('chat')

    return render(request, 'chat/chat.html', {'messages': messages, 'form': form})


@login_required
def conversation_list(request):
    conversations = Conversation.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'chat/conversation_list.html', {'conversations': conversations})

@login_required
def view_conversation(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id, user=request.user)
    messages = conversation.messages.order_by('timestamp')
    return render(request, 'chat/view_conversation.html', {'conversation': conversation, 'messages': messages})

@login_required
def delete_conversation(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id, user=request.user)
    conversation.delete()
    messages.success(request, "Conversation deleted successfully.")
    return redirect('conversation_list')
