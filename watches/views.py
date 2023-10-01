from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from .models import Category, Item, Offer
from conversation.models import Conversation, ConversationMessage


def filtered_items(request, category_name=None):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    min_year = request.GET.get('min_year')
    max_year = request.GET.get('max_year')

    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_name:
        # Filter by category name if provided
        items = items.filter(category__name=category_name)

    if category_id:
        # Filter by category_id if provided
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    # Apply price filter if both min_price and max_price are provided
    if min_price and max_price:
        items = items.filter(price__range=(min_price, max_price))
    elif min_price:
        items = items.filter(price__gte=min_price)
    elif max_price:
        items = items.filter(price__lte=max_price)

    # Apply year filter if both min_year and max_year are provided
    if min_year and max_year:
        items = items.filter(year__range=(min_year, max_year))
    elif min_year:
        items = items.filter(year__gte=min_year)
    elif max_year:
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
        'category_name': category_name, 
    })



def search_items(request):
    query = request.GET.get('query', '')

    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)  

    if query:
        items = items.filter(
            Q(name__icontains=query) |  # item name
            Q(description__icontains=query)  # item description
        )

    

    # Redirect back to the main items view after searching
    return render(request, 'watches/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'min_price': None,  
        'max_price': None,
        'min_year': None,
        'max_year': None,
    })



def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    categories = Category.objects.all()

    return render(request, 'watches/detail.html', {
        'item': item,
        'related_items': related_items,
        'categories': categories,
    })

@login_required
def submit_offer(request, pk):
    item = get_object_or_404(Item, pk=pk)
    categories = Category.objects.all()

    if request.method == 'POST':
        offer_amount = request.POST.get('offer_amount')

        # Create a new conversation for the offer
        conversation = Conversation.objects.create(item=item)
        conversation.members.add(request.user)
        conversation.members.add(item.created_by)

        # Create the offer message within the conversation
        offer_message = ConversationMessage.objects.create(
            conversation=conversation,
            content = f"I would like to offer : £{offer_amount}.",
            created_by=request.user,
            is_offer=True  # Set this as an offer message
        )

        categories = Category.objects.all()

        return render(request, 'watches/thanks.html', {'item': item, 'categories': categories})

    return render(request, 'watches/submit_offer.html', {'item': item, 'categories': categories})






