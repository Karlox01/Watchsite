from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from .models import Category, Item, Offer
from conversation.models import Conversation, ConversationMessage


def filtered_items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    min_year = request.GET.get('min_year')
    max_year = request.GET.get('max_year')

    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    if min_price:
        items = items.filter(price__gte=min_price)

    if max_price:
        items = items.filter(price__lte=max_price)

    if min_year:
        items = items.filter(year__gte=min_year)

    if max_year:
        items = items.filter(year__lte=max_year)

    return render(request, 'watches/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
        'min_price': min_price,
        'max_price': max_price,
        'min_year': min_year,
        'max_year': max_year,
    })




def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'watches/detail.html', {
        'item': item,
        'related_items': related_items
    })

@login_required
def submit_offer(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        offer_amount = request.POST.get('offer_amount')

        # Create a new conversation for the offer
        conversation = Conversation.objects.create(item=item)
        conversation.members.add(request.user)
        conversation.members.add(item.created_by)

        # Create the offer message within the conversation
        offer_message = ConversationMessage.objects.create(
            conversation=conversation,
            content=f"New offer for '{item.name}' received: £{offer_amount}.",
            created_by=request.user,
            is_offer=True  # Set this as an offer message
        )

        return render(request, 'watches/thanks.html')

    return render(request, 'watches/submit_offer.html', {'item': item})



