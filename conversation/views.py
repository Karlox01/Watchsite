from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from watches.models import Item
from .forms import ConversationMessageForm
from .models import Conversation
from watches.models import Offer

@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')

    # Check if a conversation with the same members already exists
    conversations = Conversation.objects.filter(item=item, members=request.user)
    
    if conversations.exists():
        # Redirect to the existing conversation
        return redirect('conversation:detail', conversations.first().id)
    
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            is_offer = form.cleaned_data.get('is_offer', False)  # Get the offer flag
            # Create a new conversation
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.is_offer = is_offer  # Set the offer flag
            conversation_message.save()

            return redirect('watches:detail', pk=item_pk)
    else:
        form = ConversationMessageForm()
    
    return render(request, 'conversation/new.html', {
        'form': form
    })


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members=request.user)

    offers = []
    for conversation in conversations:
        # Assuming there's a foreign key relationship between Conversation and Item models
        item = conversation.item  # Get the related item
        item_offers = Offer.objects.filter(item=item)  # Access the related offer directly, not as a set

        if item_offers:
            offers.extend(item_offers)

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations,
        'offers': offers,
    })


@login_required
def detail(request, pk):
    conversation = get_object_or_404(Conversation, pk=pk, members=request.user)
    form = ConversationMessageForm()

    if request.method =='POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('conversation:detail', pk=pk)

    messages = conversation.messages.all()

    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form': form,
        'messages': messages,
    })

